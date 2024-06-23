# Please write a program which asks the user to type in a number. The program then
# prints out the positive integers between 1 and the number itself, alternating between
# the two ends of the range as in the examples below.

input_integer = int(input('Please type in a number: '))
start = 1
while start <= input_integer:
    print(start)
    if input_integer != start:
        print(input_integer)
    start += 1
    input_integer -= 1
