from math import sqrt

while True:
    entry = int(input('Please type in a number:'))
    if entry == 0:
        break
    if entry != 0:
        if entry < 0:
            print('Invalid number')
        if entry > 0:
            print(sqrt(entry))

print('Exiting...')
