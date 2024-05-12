inpt = str(input('Please type in a string: '))
second = inpt[1]
second_last = inpt[-2]
if second == second_last:
    print(f'The second and the second to last characters are {second}')
elif second != second_last:
    print('The second and the second to last characters are different')
    