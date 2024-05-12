inpt = str(input('Please type in a string: '))
x = 1
while x <= len(inpt):
    print(inpt[-x:])
    x += 1