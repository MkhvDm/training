import zipfile
import requests
import os
import pandas as pd
import numpy as np


''' Downloading ZIP '''
input_url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
# resp = requests.get(input_url)
# if (resp.status_code != 200):
#     print('Connection error!')
# else:
#     with open('salaries_archive.zip', 'wb') as zip_file:
#         zip_file.write(resp.content)

''' Extract files from ZIP '''
with zipfile.ZipFile('salaries_archive.zip','r') as zip_file:
    zip_file.extractall('salary_dir')

''' Analyze DIR '''
os.chdir('salary_dir')
list_of_files = os.listdir()

''' Walk through files '''
result_list = []
for xlsx_name in list_of_files:
    worker_df = pd.read_excel(xlsx_name, index_col=0, engine='openpyxl')
    name = worker_df.loc['ФИО'].get('Unnamed: 1')
    salary = worker_df.loc['ФИО'].get('Unnamed: 3')
    result_list.append([name, str(int(salary))])

result_df = pd.DataFrame(result_list, columns=['ФИО', 'Зарплата'])
result_df = result_df.sort_values(['ФИО'], ascending = True, kind = 'mergesort')
np.savetxt('report_np.txt', result_df.values, fmt='%s', encoding='utf-8')




