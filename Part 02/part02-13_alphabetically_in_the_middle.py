first = str(input('1st letter:'))
second = str(input('2nd letter:'))
third = str(input('3rd letter:'))

letters = sorted([first, second, third])
print(f'The letter in the middle is {letters[1]}')
