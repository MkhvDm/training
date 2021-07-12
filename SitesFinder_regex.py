import requests
from lxml import html
import re
import sys

url_input = 'http://pastebin.com/raw/hfMThaGb'
# url_input = 'http://pastebin.com/raw/7543p0ns'
# found_urls = []
correct_url_http = []
correct_url_www = []
correct_url_non = []
correct_url = []
response = requests.get(url_input)
if response.status_code != 200:
    print('Error!')
else:
    print(response.text)
    found_urls = re.findall(r'<a .*href=["\']([^"\']*)["\']', response.text)
    print(found_urls)
    print('============================')

    for url in found_urls:
        print('#')
        print('in:', url)
        filtered_url = re.search(r'(http://|https://|ftp://)([^\/:\b]+)(\/|:|.*\b)', url)
        if filtered_url != None:
            print(filtered_url.groups())
            correct_url_http.append(filtered_url.group(2))
            print('out1:', filtered_url)
        else:
            filtered_url = re.match(r'(www\.[^\/:\b]+)', url)
            if filtered_url != None:
                print(filtered_url.groups())
                correct_url_www.append(filtered_url.group(1))
                print('out2:', filtered_url)
            else:
                filtered_url = re.match(r'(\b[^\/:\b]+)', url)
                if filtered_url != None:
                    print(filtered_url.groups())
                    correct_url_non.append(filtered_url.group(1))
                    print('out3:', filtered_url)
print(found_urls)
print(correct_url_http)
print(correct_url_www)
print(correct_url_non)
correct_url.extend(correct_url_http)
correct_url.extend(correct_url_www)
correct_url.extend(correct_url_non)

correct_url_set = set(correct_url)
correct_url_set = sorted(correct_url_set)
print(*correct_url_set, sep='\n')