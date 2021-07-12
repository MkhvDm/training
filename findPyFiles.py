import os
import os.path
with open('RESULT.txt', 'w') as out_file:
    for currentDir, dirs, files in os.walk('main'):
        for file in files:
            if file.endswith('.py'):
                out_file.write(currentDir + '\n')
                break
with open('RESULT.txt', 'r') as out_file:
    print(out_file.read())




