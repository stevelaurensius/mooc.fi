# Please write a program which asks the user for words. If the user types in a word for the
# second time, the program should print out the number of different words typed in, and
# exit.

list_result = []
while True:
    input_string = str(input('Word: '))
    if input_string in list_result:
        break
    list_result.append(input_string)
print(f'You typed in {len(list_result)} different words')
