"""
String manipulations
Indexing and slicing of strings
String concatenation and multiplication
String interpolation
"""

# print("hello \n world")
# print("hello \nworld")
# print(len("hello \n world"))


'''

'''
# positive indexing
my_string = "Hello World"
print(id(my_string))
print(my_string)
print(my_string[0])
print(my_string[6])

# negative indexing
print(my_string[-3])
print(my_string[-5])

# slicing
print(my_string[2:])
print(my_string[:6])
print(my_string[2:6])
print(my_string[::])
print(my_string[::2])
print(my_string[::5])

# string properties and methods
# string concatenation

my_string1 = "Helo World"
print(my_string1)
my_string1_manipulated = my_string1[1:]
print(my_string1_manipulated)
print('B'+my_string1_manipulated)

capture_my_string1_index1 = my_string1[0]
capture_my_string1_index1 = 'B'
print(capture_my_string1_index1+my_string1_manipulated)

# multiply the character
print(10*'a')

# converts string to upper case
print(my_string1.lower())

# Tells as what the upper class is all about
print(my_string1.upper)

# Splits the string into list
print(my_string1.split('l'))

# String interpolation
print('Hello {}'.format('Harish'))
# String interpolation with index numbers
print('{1} {3} {2} {0} {4}'.format('little', 'Mary', 'the', 'made', 'lamp'))
# String interpolation with keywords
print('{M} {m} {t} {l} {a}'.format(l='little', M='Mary', t='the', m='made', a='lamp'))

# String interpolation using F- Strings
name = 'Harish'
print(f'Hello {name}')



