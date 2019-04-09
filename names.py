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
first_name_map = {}
for wedding in weddings:
    if wedding['url'] in wedding_keys:
        #print ("Skipping repeat ", wedding['names'])
        continue

    names = wedding['names'].split(',')
    name1 = names[0].strip().split(" ")[0];
    name2 = names[1].strip().split(" ")[0]
    first_names = name1 + " and " + name2
    first_name_list.append(first_names)
    # print (first_names)

    if name1 in first_name_map:
        first_name_map[name1].append(name2)
    else:
        first_name_map[name1] = [name2]

    summary = wedding['summary']
    wedding_keys.add(wedding['url'])
    #print (summary.split('.')[0])

for name1 in sorted(first_name_map.keys()):
    print (name1, "and",", ".join(first_name_map[name1]))
