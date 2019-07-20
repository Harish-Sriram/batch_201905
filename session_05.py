'''
Dictionary
Set
Tuple
Types of function(with and without parameters and or return value
unnamed and named parameters
Create user defined functions
Anonymous lambda functions
'''
# Var_dict = {
#     'key0': 'Value0'
# }
# Var_dict['key1'] = 'value1'
# Var_dict.update({
#     'key2': 'value2',
#     'key3': 'value3'
# })
# for key in Var_dict.keys():
#     print(key)
# print(Var_dict.get('key4', 'Key does not exist'))
# print(Var_dict.keys())
# print(Var_dict.values())
# Var_dict.pop('key0')
# print(Var_dict)
# tuple example
# Var_tuple = (1,1,1)
# print(Var_tuple)
# set example
# Var_set = set([1,2,3,4,1,1,1,1,1,1,1])
# print(Var_set)


# define functions
# def funct():
#     print("Hello Vaidyanathan")
# funct()
#
# def funct1(name):
#     return "Hello {}....!!!".format(name)
# funct1('Harish')
# funct1('Vaidyanathan')
# def addition(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# def calculator(operation):
#
#     if operation in ['Add', '+', 'Addition']:
#         print(addition(4, 3))
#     elif operation in ['Sub', '-', 'Subtraction']:
#         print(subtract(4, 3))
#     elif operation in ['Mul', '*', 'Multiplication']:
#         print(multiply(4, 3))
# calculator('*')
# wildcard operator only for list and dictonary
# def cal_03(**test):
#     operation = test.get('operation')
#     if operation in ['Add', '+', 'Addition']:
#         return sum(test.get('numbers'))
#     elif operation in ['Sub', '-', 'Subtraction']:
#         return test.get('x',0) - test.get('y',0)
# x = cal_03(**{
#     'operation': 'Add',
#     'numbers': [10,3,5]
# })
# print(x)
# #anonymous lamda function
# power = lambda a: a*a
# # print(power(a=5))
# _list = [1,2,3,4]
# odd = list(map(lambda x: power(x), _list))
# print(odd)