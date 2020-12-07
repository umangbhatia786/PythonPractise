from csv import DictReader

file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\CSV\address.csv'

with open(file_path) as file:
    csv_dict = DictReader(file)

    for row in csv_dict:
        print(row)