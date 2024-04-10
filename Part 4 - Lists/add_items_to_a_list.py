# Please write a program which first asks the user for the number of items to be added.
# Then the program should ask for the given number of values, one by one, and add them
# to a list in the order they were typed in. Finally, the list is printed out.

list_result = []
input_integer = int(input('How many items: '))
item_counter = 1
while input_integer > 0:
    input_append = int(input(f'Item {item_counter}: '))
    list_result.append(input_append)
    item_counter += 1
    input_integer -= 1
print(list_result)
