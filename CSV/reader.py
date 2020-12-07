from csv import reader

file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\CSV\address.csv'
with open(file_path) as file:
    csv_reader = reader(file)
    csv_rows = list(csv_reader)
    '''for row in csv_reader:
        print(row)'''

    print(csv_rows)

    