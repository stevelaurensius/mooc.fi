# Please write a program which asks the user to choose between addition and removal.
# Depending on the choice, the program adds an item to or removes an item from the end of
# a list. The item that is added must always be one greater than the last item in the list. The
# first item to be added must be 1.

list_result = []
print(f'The list is now {list_result}')
while True:
    input_command = input('a(d)d, (r)emove or e(x)it: ')
    if input_command == 'x':
        break
    if input_command == 'd':
        list_result.append(len(list_result) + 1)
        print(f'The list is now {list_result}')
    if input_command == 'r':
        list_result.remove(len(list_result))
        print(f'The list is now {list_result}')
print('Bye!')
