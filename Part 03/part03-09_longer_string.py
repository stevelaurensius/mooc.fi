string_1 = str(input('Please type in string 1: '))
string_2 = str(input('Please type in string 2: '))
if len(string_1) > len(string_2):
    print(f'{string_1} is longer')
elif len(string_2) > len(string_1):
    print(f'{string_2} is longer')
else:
    print('The strings are equally long')
