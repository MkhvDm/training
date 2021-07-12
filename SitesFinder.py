import requests
from lxml import html
import re

# url_input = 'http://pastebin.com/raw/hfMThaGb'
url_input = 'http://pastebin.com/raw/7543p0ns'
correct_url = []
response = requests.get(url_input)
if response.status_code != 200:
    print('Error!')
else:
    print(response.text)
    html_DOM = html.fromstring(response.text)
    urls = html_DOM.xpath('//a/@href') #a/@href
    print(*urls, sep='\n')
    print('============================')
    for url in urls:
        print()
        print('in:', url)
        url = url.__str__()
        # url = re.sub(r'(?:http://|https://|ftp://)(.+\.\w+)(?:/*.*)', r'\1', url)
        url = re.search(r'(?:http://|https://|ftp://)([^\/:\b]+)(\/|:|.*\b)', url) #(?:http:\/\/|https:\/\/|ftp:\/\/)(.+)(\/|\b)
        # url = re.search(r'(?:http:\/\/|https:\/\/|ftp:\/\/)(.+)(?:(\/|\b))', url)
        if url != None:
            print(url.groups())
            # correct_url.append(url.group(1))
            # print(correct_url)
        print('out:', url)
print(urls)
# correct_url_set = set(correct_url)
# print(correct_url_set)
