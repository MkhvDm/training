import re
import sys

#1
# patern = r'cat.*cat'#{2,}' #{2,}'
# for line in sys.stdin:
#     line = line.rstrip()
#     result = re.search(patern, line)
#     if result:
#         print(line)
#

#2
# patern = r'\bcat\b'#{2,}' #{2,}'
# for line in sys.stdin:
#     line = line.rstrip()
#     result = re.search(patern, line)
#     if result:
#         print(line)

#3
# patern = r'z(.{3})z'
# for line in sys.stdin:
#     line = line.rstrip()
#     result = re.search(patern, line)
#     if result:
#         print(line)

#4
# patern = r'\\'
# for line in sys.stdin:
#     line = line.rstrip()
#     result = re.search(patern, line)
#     if result:
#         print(line)

#5
# patern = r'\b(\w+)\1\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     result = re.search(patern, line)
#     if result:
#         print(line)

#6
# patern = r'human'
# change = 'computer'
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(patern, change, line))

#7
# patern = r'\b(a+)\b'
# change = 'argh'
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(patern, change, line, 1, re.IGNORECASE))

#8
# patern = r'\b(\w)(\w)'
# sub_patern = r'\2.\1.'
# change = r'\2\1'
# example = ['"this\' !is. ?n1ce,', 'text&']
# out_lst = []
# print(example)
# for line in example:#sys.stdin:
#     new_out = re.sub(patern, change, line)
#     print(new_out, end='')

#9
# patern = r'(\w)(\1{1,})'
# change = r'\1'
# example = ['buzzz', 'attraction']
# print(example)
# for line in example:#sys.stdin:
#     new_out = re.sub(patern, change, line)
#     print(new_out)

#10
NUMBERS = [str(bin(i))[2:] for i in range(1000)]
# print(*NUMBERS, sep='\n')

example = ['','']
patern = r'\'
for number in NUMBERS:


    # if not int(number, 2) % 3:
    #     print(number, "%3")
    # else:
    #     print(number) #, '\tINPUT')
    # number = list(number.rstrip('0'))
    # number.reverse()
    # number = ''.join(number)
    # # print(number)


