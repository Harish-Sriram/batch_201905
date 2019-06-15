"""
1) Conditional statement
2) Looping statement
"""
'''
# If else statement example
num1 = 10
num2 = 19
if num1 < num2 :
    print("num1 is minimum")
else:
    print("num2 is minimum")

# If.. elif..else example
num1 = 3
num2 = 3
if num1 < num2 :
    print("num1 is minimum")
elif num2 < num1:
    print("num2 is minimum")
else:
    print("Both are same")
'''

# # print smallest number out of 3 numbers
# num1 = 20
# num2 = 10
# num3 = 15
# if num1 < num2 < num3:
#     print("num1 is minimum")
# elif num2 < num3:
#     print("num2 is minimum")
# else:
#     print("num3 is minimum")
#
#
# # print maximum number out of 3 numbers
# num4 = 20
# num5 = 10
# num6 = 15
# if num4 > num5 > num6:
#     print("num4 is maximum")
# elif num5 > num6:
#     print("num5 is maximum")
# else:
#     print("num6 is maximum")

num1 = 17
num2 = 9
num3 = 2
if num1 == num2 == num3:
    print("All three numbers are same")
elif num1 == num2 and num1 < num3:
    print("num1 and num 2 are minimum")
elif num1 != num2 and num1 < num2 and num3:
    print("num 1 is minimum")
elif num1 == num3 and num1 < num2:
    print("num1 and num 3 are minimum")
elif num1 != num3 and num1 < num2 and num1 < num3:
    print("num 1 is minimum")
elif num2 == num3 and num2 < num1:
    print("num2 and num 3 are minimum")
elif num2 != num3 and num2 < num1 and num2 < num3:
    print("num 2 is minimum")
else:
    print("num3 is minimum")

'''
for iterator in <iterable object>
    <Statement 1>
    <Statement 2>
    
range(start, end, step)

while <condition>
   <Statement 1>
   <Statement 2>
'''







