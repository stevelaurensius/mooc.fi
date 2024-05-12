number_one = int(input('Number 1:'))
number_two = int(input('Number 2:'))
operation = input('Operation:')

if operation == 'add':
    print(f'{number_one} + {number_two} = {number_one + number_two}')

if operation == 'multiply':
    print(f'{number_one} * {number_two} = {number_one * number_two}')

if operation == 'subtract':
    print(f'{number_one} - {number_two} = {number_one - number_two}')
