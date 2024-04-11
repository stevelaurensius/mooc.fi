# Please write a program which asks the user to type in a string. The program then
# prints each input character on a separate line. After each character there should
# be a star (*) printed on its own line.
input_string = str(input('Please type in a string: '))
for i in input_string:
    print(i)
    print('*')
