# Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. Then
# the program should ask the user for an index and a new value, replace the value at the
# given index, and print the list again. This should be looped over until the user gives -1 for
# the index. You can assume all given index values will fall within your list.

list_value = [1, 2, 3, 4, 5]
while True:
    input_index = int(input('Index: '))
    if input_index == -1:
        break
    new_value = int(input('New value: '))
    list_value[input_index] = new_value
    print(list_value)