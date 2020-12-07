from csv import reader,DictWriter
import csv

file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\CSV\details.csv'

print('***************** CSV Before Writing Data ***************')

with open(file_path) as file:
    csv_reader = reader(file)

    for row in csv_reader:
        print(row)

with open(file_path,'a') as file:
    headers = ['Name', 'Age', 'City', 'Religion']
    csv_reader = DictWriter(file, fieldnames= headers)
    csv_reader.writerow({'Name':'Harsh', 'Age': '25', 'City': 'Ranchi', 'Religion': 'Hinduism'})

print('***************** CSV After Writing Data ***************')

with open(file_path) as file:
    csv_reader = reader(file)

    for row in csv_reader:
        print(row)