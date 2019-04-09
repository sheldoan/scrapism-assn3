import requests
import json
import time
import csv

csv_file = open('data.csv', mode='w')
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(['headline', 'url', 'date', 'summary', 'thumb_image_url', 'big_image_url'])
error_file = open('json_on_error.html', 'w')

#cursor = "YXJyYXljb25uZWN0aW9uOjE1OQ"
#cursor = "YXJyYXljb25uZWN0aW9uOjE1MjU=" # after 1520 scanned
cursor = "YXJyYXljb25uZWN0aW9uOjU2NQ" #after 560 scanned

num_stories = 0
num_stories_without_images = 0
while True:
    headers = {
        'Origin': 'https://www.nytimes.com',
        'nyt-token': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlYOpRoYg5X01qAqNyBDM32EI/E77nkFzd2rrVjhdi/VAZfBIrPayyYykIIN+d5GMImm3wg6CmTTkBo7ixmwd7Xv24QSDpjuX0gQ1eqxOEWZ0FHWZWkh4jfLcwqkgKmfHJuvOctEiE/Wic5Qrle323SMDKF8sAqClv8VKA8hyrXHbPDAlAaxq3EPOGjJqpHEdWNVg2S0pN62NSmSudT/ap/BqZf7FqsI2cUxv2mUKzmyy+rYwbhd8TRgj1kFprNOaldrluO4dXjubJIY4qEyJY5Dc/F03sGED4AiGBPVYtPh8zscG64yJJ9Njs1ReyUCSX4jYmxoZOnO+6GfXE0s2xQIDAQAB',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'nyt-app-type': 'project-vi',
        'content-type': 'application/json',
        'accept': '*/*',
        'Referer': 'https://www.nytimes.com/section/fashion/weddings',
        'nyt-app-version': '0.0.3',
        'DNT': '1',
    }

    data = '{"operationName":"CollectionsQuery","variables":{"id":"/section/fashion/weddings","first":10,"query":{"sort":"newest","text":""},"exclusionMode":"NONE","cursor":"%s"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"c1ff24262f450f35267e04bd84399c0b3b8a97de659ba7a668841942535d0ab3"}}}' % cursor

    response = requests.post('https://samizdat-graphql.nytimes.com/graphql/v2', headers=headers, data=data)
    full_resp = json.loads(response.text)
    try:
        wedding_stories = full_resp['data']['legacyCollection']['stream']['edges']
    except TypeError:
        error_file.write(response.text)
        print("Type error! Going to retry cursor ", cursor);
        continue
        sleep(1)


    for story in wedding_stories:
        story_headline = story['node']['headline']['default']
        story_url = story['node']['url']
        story_date = story['node']['firstPublished']
        story_summary = story['node']['summary']
        headline_parts = story_headline.split(",")

        is_couple = False
        if len(headline_parts) == 2:
            if len(headline_parts[0].split(" ")) <= 3 and len(headline_parts[1].strip().split(" ")) <= 3:
                is_couple = True
        # print(story_headline) if is_couple else print(">>> Not couple: ", story_headline)
        num_stories += 1

        if not is_couple:
            continue

        try:
            renditions = story['node']['promotionalMedia']['crops'][0]['renditions']
            thumb_url = renditions[0]['url']
            image_url = renditions[-1]['url']
            csv_writer.writerow([story_headline, story_url, story_date, story_summary, thumb_url, image_url])
            # print(image_url)
        except TypeError:
            #print("***", story_summary, " has no image. ", num_stories_without_images, "/", num_stories)
            num_stories_without_images += 1
            pass

        if num_stories % 20 == 0:
            print (cursor, "...", num_stories, " scanned, ", num_stories_without_images, " without images")


    cursor = full_resp['data']['legacyCollection']['stream']['pageInfo']['endCursor']
    if not full_resp['data']['legacyCollection']['stream']['pageInfo']['hasNextPage']:
        print ("There is no next page!! ")
        break

    time.sleep(1)
