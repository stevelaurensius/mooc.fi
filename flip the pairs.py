# Please write a program which asks the user to type in a number. The program then
# prints out all the positive integer values from 1 up to the number. However, the order
# of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes
# before 1, 4 before 3 and so forth. See the examples below for details.

input_integer = int(input('Please type in a number: '))
last_even = input_integer - (input_integer % 2)
odd = 1
even = 2
while even <= last_even:
    print(even)
    print(odd)
    odd += 2
    even += 2

if input_integer != last_even:
    print(input_integer)