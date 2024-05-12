while True:
    inpt = str(input('Please type in a string: '))
    if len(inpt) > 0:
        print(inpt)
        print('-' * len(inpt))
    else:
        break
