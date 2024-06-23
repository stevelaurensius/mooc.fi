first = str(input('Please type in the 1st word:'))
second = str(input('Please type in the 2nd word:'))
if first < second:
    print(f'{second} comes alphabetically last.')
elif first > second:
    print(f'{first} comes alphabetically last.')
else:
    print('You gave the same word twice.')
    