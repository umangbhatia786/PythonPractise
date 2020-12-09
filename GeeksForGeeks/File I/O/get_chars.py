#Python code to get number of characters, spaces and lines in a txt file

def get_properties(file_path):
    '''Function to get text file attributes like lines, space count and char count'''
    with open(file_path) as f:
        file_content = f.readlines()

    lines_count = len(file_content)
    space_count = 0
    char_count = 0
    for line in file_content:
        for char in line:
            if char == ' ':
                space_count += 1
            else:
                char_count += 1
    return lines_count, space_count, char_count

my_path = 'GeeksForGeeks\File I\O\get_chars.txt'
properties_tuple = get_properties(my_path)

print('The properties for the given file is: ')
print(f'Line count: {properties_tuple[0]}, Space Count: {properties_tuple[1]} and Char Count: {properties_tuple[2]}')

