input_string = input('Please type in a string: ')
substring = input('Please type in a substring: ')
first_occur = input_string.find(substring)
input_string = input_string[first_occur + len(substring):]
second_occur = input_string.find(substring)
if second_occur < 0:
    print('The substring does not occur twice in the string.')
else:
    print(f'The second occurrence of the substring is at index {first_occur + second_occur + len(substring)}.')
