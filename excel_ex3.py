import requests
import pandas as pd
import numpy as np
import math

''' Downloading Excel file: '''
input_url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
resp = requests.get(input_url)
if (resp.status_code != 200):
    print('Connection error!')
else:
    with open('day_ration.xlsx', 'wb') as xl_file:
        xl_file.write(resp.content)


''' XLSX to DataFrame '''
nutrition_facts_df = pd.read_excel('day_ration.xlsx', 'Справочник',  index_col=0, engine='openpyxl')
day_ration_df = pd.read_excel('day_ration.xlsx', 'Раскладка',  index_col=0, engine='openpyxl')

sum_ration = {'kkal': 0, 'protein': 0, 'fat': 0, 'carbo': 0}

for product in day_ration_df.iterrows():
    name = product[0]
    weight = product[1].get('Вес в граммах')
    kkal_100g = nutrition_facts_df.loc[name, 'ККал на 100']
    protein_100g = nutrition_facts_df.loc[name, 'Б на 100']
    fat_100g = nutrition_facts_df.loc[name, 'Ж на 100']
    carbo_100g = nutrition_facts_df.loc[name, 'У на 100']
    carbo_100g = 0 if np.isnan(carbo_100g) else carbo_100g

    sum_ration['kkal']    += weight * kkal_100g / 100
    sum_ration['protein'] += weight * protein_100g / 100
    sum_ration['fat']     += weight * fat_100g / 100
    sum_ration['carbo']   += weight * carbo_100g / 100

for key in sum_ration.keys():
    sum_ration[key] = math.floor(sum_ration[key])
print(*sum_ration.values())
