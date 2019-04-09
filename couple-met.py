import csv
import spacy

csv_file = open('data.csv')
csv_reader = csv.DictReader(csv_file)

nlp = spacy.load('en_core_web_sm')

weddings = []
for row in csv_reader:
    weddings.append(row)

wedding_keys = set()
for wedding in weddings:
    if wedding['url'] in wedding_keys:
        continue

    summary = wedding['summary']
    doc = nlp(summary)
    sents = list(doc.sents)
    if len(sents) > 0:
        first_sentence = sents[0]
        print(first_sentence)

    wedding_keys.add(wedding['url'])
