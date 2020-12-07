from csv import reader,writer
import csv

file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\CSV\details.csv'

print('***************** CSV Before Writing Data ***************')

with open(file_path) as file:
    csv_reader = reader(file)

    for row in csv_reader:
        print(row)

with open(file_path,'a') as file:
    csv_reader = writer(file)
    csv_reader.writerow(['Shahid','27', 'Lucknow', 'Islam'])

print('***************** CSV After Writing Data ***************')

with open(file_path) as file:
    csv_reader = reader(file)

    for row in csv_reader:
        print(row)


