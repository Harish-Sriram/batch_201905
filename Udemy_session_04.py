# Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
split_words = st.split()
#print(split_words, end='')
for word in split_words:
    if word[0] == 's':
        print(word, end=' ')
print('\n')

# Use range() to print all the even numbers from 0 to 10.
for i in range(0, 11):
    if i%2 == 0:
        print(i, end=' ')

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('\n')
list1 = [i for i in range(1, 51) if i%3 == 0]
print(list1, end=' ')

# Go through the string below and if the length of a word is even print \"even!\
print('\n')
st1 = 'Print every word in this sentence that has an even number of letters'
split_even_words = st1.split()
for even_words in split_even_words:
    word_length = len(even_words)
    if word_length%2 == 0:
        print('Word: {}\n Length: {} <-- has an even length!'.format(even_words, word_length))

#Write a program that prints the integers from 1 to 100. But for multiples of three print \"Fizz\" instead of the number, and for the multiples of five print \"Buzz\". For numbers which are multiples of both three and five print \"FizzBuzz\
for integer in range(1, 101):
    if integer%3 == 0 and integer%5 == 0:
        print("FizzBuzz", end=' ')
    elif integer%3 == 0:
        print("Fizz", end=' ')
    elif integer%5 == 0:
        print("Buzz", end=' ')
    else:
        print(integer, end=' ')
print('\n')

# Use List Comprehension to create a list of the first letters of every word in the string below:

st2 = 'Create a list of the first letters of every word in this string'
# print(type(st2.split()))
list2 = []
for first_letter in st2.split():
    list2.append(first_letter[0])
print(list2)

list3 = [first_letter[0] for first_letter in st2.split()]
print(list3)

