import requests
import pandas as pd
import numpy as np
import math

import time
start_time = time.time()

''' Downloading Excel file: '''
# input_url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'
# resp = requests.get(input_url)
# if (resp.status_code != 200):
#     print('Connection error!')
# else:
#     with open('hike_ration.xlsx', 'wb') as xl_file:
#         xl_file.write(resp.content)

''' XLSX to DataFrame '''
hike_ration_df = pd.read_excel('hike_ration.xlsx', 'Раскладка',  index_col=0, engine='openpyxl').fillna(0)
nutrition_facts_df = pd.read_excel('hike_ration.xlsx', 'Справочник',  index_col=0, engine='openpyxl').fillna(0)

set_of_days = set(hike_ration_df.index.values)

sum_ration_df = pd.DataFrame(columns=['kkal', 'protein', 'fat', 'carbo'])
sum_ration = {'kkal': 0, 'protein': 0, 'fat': 0, 'carbo': 0}

for day_num in set_of_days:
    sum_ration = sum_ration.fromkeys(sum_ration, 0)
    day_df = hike_ration_df.loc[day_num]
    for prod in day_df.iterrows():
        print('++++++', prod, '+++++++')
        name = prod[1].get('Продукт')
        weight = prod[1].get('Вес в граммах')
        kkal_100g = nutrition_facts_df.loc[name, 'ККал на 100']
        protein_100g = nutrition_facts_df.loc[name, 'Б на 100']
        fat_100g = nutrition_facts_df.loc[name, 'Ж на 100']
        carbo_100g = nutrition_facts_df.loc[name, 'У на 100']

        sum_ration['kkal']    += weight * kkal_100g / 100
        sum_ration['protein'] += weight * protein_100g / 100
        sum_ration['fat']     += weight * fat_100g / 100
        sum_ration['carbo']   += weight * carbo_100g / 100
    for key in sum_ration.keys():
        sum_ration[key] = math.floor(sum_ration[key])
    sum_ration_df.loc[day_num] = list(sum_ration.values())

for row in sum_ration_df.values:
    print(*row)

print("--- %s seconds ---" % (time.time() - start_time))
