# Please write a program which asks for the name of the user and then creates an
# "inscription" in a file specified by the user. Please see the example below.


recipient = input('Whom should I sign this to: ')
filename = input('Where shall I save it: ')

with open(filename, "w") as file:
    file.write(f'Hi {recipient}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')
