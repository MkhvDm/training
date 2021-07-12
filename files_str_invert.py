
import os
# os.path.join('D','Python', 'test_proj','venv')

with open('input_file.txt', 'r') as my_file, open('output_file.txt', 'w') as output_file:
    tmp = my_file.readlines()
    tmp.reverse()
    for string in tmp:
        output_file.write(string.strip() + '\n')