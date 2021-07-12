import os
import requests
from bs4 import BeautifulSoup

input_url = 'https://stepik.org/media/attachments/lesson/209723/5.html'
sum = 0

resp = requests.get(input_url)

if (resp.status_code != 200):
    print('Connection error!')
else:
    my_tree = BeautifulSoup(resp.text, 'lxml')
    # print(my_tree)
    for tag in my_tree.find_all('td'):
        print(tag)
        print()
        sum += int(tag.get_text())
print(sum)




