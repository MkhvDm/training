import requests
import json

with open('dataset_24476_3.txt', 'r') as input_file:
    numbers = input_file.read().splitlines()

req_url = 'http://numbersapi.com/{}/math?default=Boring'

for number in numbers:
    resp = requests.get(req_url.format(number))
    if resp.status_code != 200:
        print('Error:', resp.status_code)
    elif resp.text == 'Boring':
        print('Boring')
    else:
        print('Interesting')