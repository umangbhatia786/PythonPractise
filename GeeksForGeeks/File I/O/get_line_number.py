#Python Code to get line numbers where a specified word is present

def get_lines_list(file_path, word):
    '''Python Function to get a list of line numbers where a given word is present'''
    with open(file_path) as f:
        file_content = f.readlines()

    line_num_list = list()
    for i in range(len(file_content)):
        if word in file_content[i]:
            line_num_list.append(f'Line {i+1}')

    return line_num_list

my_path = 'GeeksForGeeks\File I\O\get_chars.txt'
print(get_lines_list(my_path, 'line'))
