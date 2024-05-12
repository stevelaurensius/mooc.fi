input_string = input('Please type in a word: ')
char_find = input('Please type in a char: ')

index = input_string.find(char_find)

# Check if the character is found in the input string
if index != -1:
    while index != -1:
        # Check if there are at least 3 characters remaining after the found index
        if len(input_string) - index >= 3:
            result = input_string[index:index + 3]
            print(result)
        # Find the next occurrence of the character
        index = input_string.find(char_find, index + 1)
else:
    pass
