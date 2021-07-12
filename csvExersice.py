import csv
import sys

crime_type_dict = {}
'''
crime_type_stats[0] -- type
crime_type_stats[1] -- number of cases
'''

with open("Crimes.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if '2005' in row[2]:
            dict_value = crime_type_dict.setdefault(row[5], 0)
            crime_type_dict.update({row[5] : dict_value + 1})

crime_type_dict = sorted(crime_type_dict, key = crime_type_dict.get)
crime_type_dict.reverse()
print(crime_type_dict)