"""
Create score board
implement LIST

"""

'''
runs = 0
wickets = 0
max_wickets = 10
overs = 0
max_overs = 1
no_of_balls_in_a_over = 6
current_ball_in_over = 0
types_of_runs = ['1', '2', '3', '4', '5', '6']
types_of_extras = ['wd', 'nb']
types_of_wickets = ['lbw', 'b', 'c', 'ro', 'stump', 'htw']
print(F"Types of runs: {','.join(types_of_runs)}")
print(F"Types of wickets: {','.join(types_of_wickets)}")
print('-------------------------')
print(F'{runs}/{wickets}')
print(F'{overs}.{current_ball_in_over}({max_overs})')
print('-------------------------')
while True:
    if wickets == 10 or overs == max_overs:
        break
    input_Runs = str(input("Enter runs!!")).strip()
    if input_Runs in types_of_extras:
        runs += 1
    elif input_Runs in types_of_runs:
        runs += int(input_Runs)
        current_ball_in_over += 1
    elif input_Runs in types_of_wickets:
        wickets += 1
        current_ball_in_over += 1
    else:
        print("invalid input")

    if current_ball_in_over == no_of_balls_in_a_over:
        overs += 1
        current_ball_in_over = 0
    print('-------------------------')
    print(F'{runs}/{wickets}')
    print(F'{overs}.{current_ball_in_over}({max_overs})')
    print('-------------------------')
totalRuns = runs
totalWicketsLost = wickets
print("Total runs made", totalRuns)
print("Total wickets lost", wickets)
'''

# # solution for a
# for i in range(0, 5):
#     for j in range(0, 5):
#         print('*', end='')
#     print("")
#
# # solution for  b
# for i in range(0, 5):
#     for j in range(0, 5):
#         print('1', end='')
#     print("")
#
# # solution for c
# for i in range(0, 5):
#     for j in range(0, 5):
#         print(F"{i%2}", end='')
#     print("")
#
# # solution for e
# for i in range(1, 6):
#     for j in range(1, 6):
#         if j <= i:
#             print(F"{j%2}", end='')
#     print("")
#
# # solution for d
# for i in range(0, 5):
#     for j in range(0, 5):
#         if j <= i:
#             print(F"{(i+j)%2}", end='')
#     print("")

# solution for f
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end='')
#     print("")


# solution for  h
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i <= j:
#             print(F"{j%2}", end='')
#     print("")
#
# # solution to G
# for i in range(0, 5):
#     for j in range(1, 6):
#         result = j+(5*i)
#         if result <= 9:
#             print('0', end='')
#             print(j+(5*i), end=' ')
#         else:
#             print(j + (5 * i), end=' ')
#     print("")

# solution for l
# for i in range(1, 7):
#     for j in range(1, 7):
#         if j <= i:
#             result1 = 2 ** j
#             print(result1, end=' ')
#
#     print("")

# solution for k
# for i in range(1, 4):
#     for j in range(1, 6):
#         result = i*j
#         if result <= 9:
#             print('0', end='')
#             print(result, end=' ')
#         else:
#             print(result, end=' ')
#     print("")
#     for x in range(5, 0, -1):
#         result1 = x * i
#         if result1 <= 9:
#             print('0', end='')
#             print(result1, end=' ')
#         else:
#             print(result1, end=' ')
#     print("")

# solution for i
# for i in range(4, 0, -1):
#     space = " "*i
#     print(space, end="")
#     for j in range(5, i, -1):
#         print("1", end=" ")
#     print()

# solution for j
# for i in range(1, 6):
#     print('*', end='')
#     space = " "*i
#     print(space, end='')
#     for j in range(i, 4):
#         if i == 1 and j == 2:
#             print(space, end=' ')
#         elif j == 3:
#             print('*', end='')
#         else:
#             print('*', end=' ')
#     if i == 4:
#         space = " "*(i-1)
#         print(space, end='')
#     elif i == 5:
#         space = " "*(i-3)
#         print(space, end='')
#     else:
#         print(space, end='')
#     print('*', end='')
#     print(" ")



# solution for m

# space = " "
# for x in range(1, 10):
#     if(x == 1) or (x == 9):
#         print('*', end='')
#     else:
#         print(space, end='')
# print("")
# for i in range(1, 5):
#     print('*', end='')
#     space = " "*i
#     print(space, end='')
#     for j in range(i, 4):
#         if i == 1 and j == 2:
#             print(space, end=' ')
#         elif j == 3:
#             print('*', end='')
#         else:
#             print('*', end=' ')
#     if i == 4:
#         space = " "*(i-1)
#         print(space, end='')
#     elif i == 5:
#         space = " "*(i-3)
#         print(space, end='')
#     else:
#         print(space, end='')
#     print('*', end='')
#     print(" ")

# solution for n
