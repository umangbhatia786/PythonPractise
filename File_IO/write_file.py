file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\File_IO\sample.txt'

with open(file_path, 'a') as file:
    file.writelines('\nOne more new line')

with open(file_path,'r') as file:
    file_content = file.read()
    print(file_content)