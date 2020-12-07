file = open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\File_IO\sample.txt','r')

#Printing The Content after reading the file
print(file.read())

#Reading again will print nothing as Cursor is set to last
print(file.read())

#We will set the cursor to original position using seek method
file.seek(0)

#Now reading content again
print(file.read())

file.close()


