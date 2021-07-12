import xlrd
import requests
import statistics

''' Downloading Excel file: '''
input_url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
resp = requests.get(input_url)
if (resp.status_code != 200):
    print('Connection error!')
else:
    with open('salaries.xlsx', 'wb') as xl_file:
        xl_file.write(resp.content)

''' Analyze Excel file: '''
book = xlrd.open_workbook('salaries.xlsx') #formatting_info=True
sheet = book.sheet_by_index(0)
db_cities, db_job, medians = {}, {}, {}

for colnum in range(1, sheet.ncols):
    col = sheet.col_values(colnum)
    db_job.update({col[0]: statistics.mean(col[1:])})
print(max(db_job, key=lambda x: db_job.get(x)))

for rownum in range(1, sheet.nrows):
    row = sheet.row_values(rownum)
    db_cities.update({row[0]:[]})
    for col_num in range(1, sheet.ncols):
        db_cities.get(row[0]).append(row[col_num])

for item in db_cities:
    db_cities.get(item).sort()
    medians.update({item:statistics.median(db_cities.get(item))})

print(max(medians, key=lambda x: medians.get(x)))



