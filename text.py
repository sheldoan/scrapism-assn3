import csv

csv_file = open('data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

weddings = []
count = 0
for row in csv_reader:
    if count != 0:
        weddings.append({ 'names': row[0], 'summary' : row[3], 'url' : row[1] })
    count += 1

wedding_keys = set()
first_name_list = []
for wedding in weddings:
    if wedding['url'] in wedding_keys:
        print ("Skipping repeat ", wedding['names'])
        continue

    names = wedding['names'].split(',')
    first_names = names[0].split(" ")[0] + " and " + names[1].strip().split(" ")[0]
    first_name_list.append(first_names)
    print (first_names)

    summary = wedding['summary']
    wedding_keys.add(wedding['url'])
    #print (summary.split('.')[0])
