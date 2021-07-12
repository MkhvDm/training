import requests
from lxml import html
import re
import sys

url_input = input().strip()

correct_url = []
response = requests.get(url_input)
if response.status_code != 200:
    print('Error!')
else:
    found_urls = re.findall(r'<a .*href=["\']([^"\']*)["\']', response.text)
    for url in found_urls:
        filtered_url = re.search(r'(http://|https://|ftp://)([^\/:\b]+)(\/|:|.*\b)', url)
        if filtered_url != None:
            correct_url.append(filtered_url.group(2))
        else:
            filtered_url = re.match(r'(www\.[^\/:\b]+)', url)
            if filtered_url != None:
                correct_url.append(filtered_url.group(1))
            else:
                filtered_url = re.match(r'(\b[^\/:\b]+)', url)
                if filtered_url != None:
                    correct_url.append(filtered_url.group(1))

correct_url_set = set(correct_url)
correct_url_set = sorted(correct_url_set)
print(*correct_url_set, sep='\n')