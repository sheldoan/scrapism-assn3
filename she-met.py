import csv
import sys
import spacy

nlp = spacy.load('en_core_web_sm')

csv_file = open('data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

subject = sys.argv[1]

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

    summary = wedding['summary']
    doc = nlp(summary)
    sents = list(doc.sents)
    if len(sents) > 0:
        first_sentence = sents[0].text
        year_index = first_sentence.find("in 20")
        filtered_summary = first_sentence
        if year_index > 0:
            filtered_summary = first_sentence[:year_index - 1] + first_sentence[year_index + 7:]
        suitor_data = { 'name': name2, 'summary' :  filtered_summary}
        if name1 in first_name_map:
            first_name_map[name1].append(suitor_data)
        else:
            first_name_map[name1] = [suitor_data]
    wedding_keys.add(wedding['url'])

suitor_list = sorted(first_name_map[subject], key=lambda i : len(i['summary']))
suitor_count = 0

for suitor in suitor_list:
    if not suitor['summary'].startswith("The couple met"):
        continue

    prefix = "That ended when she met "
    if suitor_count == 0:
        prefix = subject + " met "
    #print (suitor['summary'])
    print (prefix + suitor['name'] + suitor['summary'][len("The couple met"):])
    suitor_count += 1
