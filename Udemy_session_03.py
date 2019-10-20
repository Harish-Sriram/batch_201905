# # Set implementation
# #my_set = set('Mississippi')
# my_set = set('HHarish')
# my_set.update('pool')
# print(my_set)
# print("---------------------------**********************************************************---------------------------------------------")
# calculation_assignment = (((2**5)+18)*6.25)/2-56
# print(calculation_assignment)
#
# print(4 * (6 + 5))
# print(4 * 6 + 5)
# print(4 + 6 * 5)
# print(type(3 + 1.5 + 4))
#
# tuple unpacking
# my_list = [(0, 1), (2, 3), (4, 5)]
# for a,b in my_list:
#     # print(a)
#     print(b)
#
#  How to iterate through dictionary also implementing tuple unpacking
# d = {'K1': 1, 'K2': 2, 'K3': 3}
# for key, value in d.items():
#     print(value)
#
# # enumerate function
# my_list2 = ['String1', 'String2', 'String3']
# for _i in enumerate(my_list):
#     print(_i)
#
# # Zip function
# for i in zip(my_list, my_list2):
#     print(i[1][1])

# List comprehension example
my_list4 = [(0, 1), (2, 3), (4, 5)]
my_list3 = [print(a) for a,b in my_list4]

# returns character 'e' from string 'Hello'
my_string = 'Hello'
print(my_string[1])

# reverse the string using slicing
print(my_string[::-1])

# Build list in two separate ways
list1 = [0, 0, 0]
list2 = [i for i in list1]
print(list1)
print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

# sort the list below
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])

d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])


# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set1 = set(list5)
print(set1)

# Final Question: What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])


