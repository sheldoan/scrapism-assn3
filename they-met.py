import csv
import sys
import spacy
import re

nlp = spacy.load('en_core_web_sm')

csv_file = open('data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

subject = sys.argv[1]
gender = int(sys.argv[2]) # 0 for female, 1 for male

weddings = []
count = 0
for row in csv_reader:
    if count != 0:
        weddings.append({ 'names': row[0], 'summary' : row[3], 'url' : row[1] })
    count += 1

wedding_keys = set()
first_name_list = []
first_name_map = {}
for wedding in weddings:
    if wedding['url'] in wedding_keys:
        #print ("Skipping repeat ", wedding['names'])
        continue

    names = wedding['names'].split(',')
    name1 = names[0].strip().split(" ")[0];
    name2 = names[1].strip().split(" ")[0]

    if not subject.lower() in [name1.lower(), name2.lower()]:
        continue

    summary = wedding['summary']
    doc = nlp(summary)
    sents = list(doc.sents)

    subject_name = name1
    suitor_name = name2
    if gender == 1:
        subject_name = name2
        suitor_name = name1

    if len(sents) > 0:
        first_sentence = sents[0].text
        year_index = first_sentence.find("in 20")
        filtered_summary = re.sub(r' in 20[0-9][0-9]', "", first_sentence)
        filtered_summary = re.sub(r' 20[0-9][0-9]', "", filtered_summary)
        suitor_data = { 'name': suitor_name, 'summary' :  filtered_summary}
        if subject_name in first_name_map:
            first_name_map[subject_name].append(suitor_data)
        else:
            first_name_map[subject_name] = [suitor_data]
    wedding_keys.add(wedding['url'])

suitor_list = sorted(first_name_map[subject], key=lambda i : len(i['summary']))

subject_pronoun = "she"
if gender == 1:
    subject_pronoun = "he"

suitor_count = 0
line_to_print = ""
for suitor in suitor_list:
    if not suitor['summary'].startswith("The couple met"):
        continue
    print (line_to_print)
    prefix = "When that ended, " + subject_pronoun + " met "
    if suitor_count == 0:
        prefix = subject + " met "
    line_to_print = prefix + suitor['name'] + suitor['summary'][len("The couple met"):]
    suitor_count += 1

if suitor_count < 2:
    print (line_to_print)
else:
    prefix = "And finally, " + subject + " met "
    print (prefix + line_to_print[len("When that ended, " + subject_pronoun + " met "):])
