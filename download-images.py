import requests
import csv

big_image_urls = []
csv_file = open('data.csv', 'r')
csv_reader = csv.DictReader(csv_file)
for row in csv_reader:
    big_image_urls.append(row['big_image_url'])

downloaded_count = 0
skipped_count = 0
for url in big_image_urls:
    image_req = requests.get(url)
    if image_req.status_code == 200:
        with open("big_images/" + url.split('/')[-1], 'wb') as f:
            f.write(image_req.content)
            downloaded_count += 1
    else:
        skipped_count += 1

    if downloaded_count % 20 == 0:
        print ("Downloaded ", downloaded_count, " skipped ", skipped_count)
