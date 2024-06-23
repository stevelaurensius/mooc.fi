# Please write a program which asks the user to type in values and adds them to a
# list. After each addition, the list is printed out in two different ways:
# - in the order the items were added
# - ordered from smallest to greatest
# The program exits when the user types in 0.

list_result = []
sorted_list = []
while True:
    input_integer = int(input('New item: '))
    if input_integer == 0:
        break
    list_result.append(input_integer)
    sorted_list.append(input_integer)
    print(f'The list now: {list_result}')
    sorted_list.sort()
    print(f'The list in order: {sorted_list}')
print('Bye!')
