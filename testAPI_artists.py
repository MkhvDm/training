import requests
import json

with open('dataset_24476_4.txt', 'r') as input_file:
    artists_id = input_file.read().splitlines()
# artists_id = ['4d8b92b34eb68a1b2c0003f4', '4f5f64c23b555230ac0004b6', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']

class Artist:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

client_id = 'e1c3d2ae63b46bcf19cf'
client_secret = '5a6a1cc857a206bd277c3eb30481134b'
req_token_url = 'https://api.artsy.net/api/tokens/xapp_token'

token = requests.post(req_token_url,
                           data={
                                    "client_id": client_id,
                                    "client_secret": client_secret
                           }
                           )
token_json = json.loads(token.text)
token = token_json['token']

req_url = 'https://api.artsy.net/api/artists/{}'
headers = {"X-Xapp-Token" : token}

output_data = []
for id in artists_id:
    resp = requests.get(req_url.format(id), headers=headers)
    resp_json = json.loads(resp.text)
    output_data.append(Artist(resp_json['sortable_name'], resp_json['birthday']))

output_data = sorted(output_data, key=lambda x: x.name)
sorted_data = sorted(output_data, key=lambda x: x.birth_year)

print(*[i.name for i in sorted_data], sep='\n')
