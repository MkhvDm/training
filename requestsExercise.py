import requests
from lxml import html
import sys
url_1 = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
url_2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

patern = r'a href="(.)*"'
urls_in_url_1 = []
urls_in_suburl = []

try:
    response = requests.get(url_1)
    if response.status_code != 200:
        pass
        #print('Error!')
    else:
        html_DOM = html.fromstring(response.text)
        matchs = html_DOM.xpath('//a/@href')
        urls_in_url_1.extend(matchs)
        if urls_in_url_1 != ([] or None):
            for url in urls_in_url_1:
                response = requests.get(url)
                if response.status_code != 200:
                    continue
                else:
                    html_DOM = html.fromstring(response.text)
                    matchs = html_DOM.xpath('//a/@href')
                    urls_in_suburl.extend(matchs)
                    if url_2 in urls_in_suburl:
                        print('Yes')
                        break
    if url_2 not in urls_in_suburl:
        print('No')
except:
    print('No')