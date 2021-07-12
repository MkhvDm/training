# import xlrd
import requests
import pandas as pd

''' Downloading Excel file: '''
# input_url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
# resp = requests.get(input_url)
# if (resp.status_code != 200):
#     print('Connection error!')
# else:
#     with open('meal.xlsx', 'wb') as xl_file:
#         xl_file.write(resp.content)

''' XLSX to DataFrame '''
meal_df = pd.read_excel('meal.xlsx', index_col=0, engine='openpyxl')
# print(meal_df)
# print(meal_df.columns)
# print(meal_df.index)

# print(meal_df['ККал на 100'])
# print(meal_df['Б на 100'])

meal_df = meal_df.sort_index()
meal_df = meal_df.sort_values(['ККал на 100'], ascending = False, kind = 'mergesort')

out_meal_list = meal_df.index.tolist()
print(*out_meal_list, sep = '\n')



