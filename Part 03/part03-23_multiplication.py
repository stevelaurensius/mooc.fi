# Please write a program which asks the user for a positive integer number.
# The program then prints out a list of multiplication operations
# until both operands reach the number given by the user.

input_string = int(input('Please type in a number: '))
dictionary = [[x,y] for x in range(1, input_string + 1) for y in range(1, input_string + 1)]

for i in range(len(dictionary)):
    print(f'{dictionary[i][0]} x {dictionary[i][1]} = {dictionary[i][0] * dictionary[i][1]}')