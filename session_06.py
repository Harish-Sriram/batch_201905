"""
Generators
File parsing
"""
# def my_generator(start, stop, step):
#     print(start, stop, step)
#     while True:
#         if start > stop:
#             break
#         yield start
#         start += step
#
# for i in my_generator(0, 5, 1):
#     print(i)

from os import path, makedirs
print('----------------------------------------')
# current_file = path.abspath(__file__)
# current_directory = path.basename(current_file)
# print(current_directory)
print('----------------------------------------')
current_file1 = path.abspath(__file__)
print(current_file1)
current_directory1 = path.dirname(current_file1)
print(current_directory1)


parser_dir = path.join(current_directory1, 'file_parser')
# to check the file exist or not

if not path.exists(parser_dir):
    makedirs(parser_dir)

# lets create the file
text_file_path = path.join(parser_dir, 'text.txt')
# _file = open(text_file_path, 'w+')
# _file.write('This is text file')
# _file.close()

with open(text_file_path, 'w+') as _file:
    _file.writelines("This is text file")

with open(text_file_path, 'r+') as _file:
    for i in _file.readlines():
        print(i)

# lets create CSV file
test_data = ['test1', 'test2', 'test3', 'test4']
import csv
csv_file_path = path.join(parser_dir, 'CSV_file.csv')
with open(csv_file_path, 'w+') as _file:
    _writer = csv.writer(_file)
    _writer.writerow(test_data)

with open(csv_file_path, 'r+') as _file:
    _reader = csv.reader(_file)
    for i in _reader:
        print(i)
# writing JSON

dictionary = {
    'test': 'value1',
    'test1': {'key_1': 'value_1'},
    'test2': ['value 3']
}

from json import dump, load
json_file_path = path.join(parser_dir, 'JSON_file.json')
with open(json_file_path, 'w+') as _file:
    dump(dictionary, _file)
with open(json_file_path, 'r+') as _file:
    print(load(_file))