input_string = str(input('Please type in a word: '))
char_find = str(input('Please type in a char: '))
index = input_string.find(char_find)
result = input_string[index:(index + 3)]
if len(result) >= 3:
    print(result)
else:
    pass
