import requests
import json
import time

cursor = "YXJyYXljb25uZWN0aW9uOjE1OQ"

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
    wedding_stories = full_resp['data']['legacyCollection']['stream']['edges']
    for story in wedding_stories:
        print(story['node']['headline']['default'])

    cursor = full_resp['data']['legacyCollection']['stream']['pageInfo']['endCursor']
    time.sleep(0.5)
