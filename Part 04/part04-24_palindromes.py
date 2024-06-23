# Please write a function named palindromes, which takes a string
# argument and returns True if the string is a palindrome.
# Palindromes are words which are spelled exactly the same
# backwards and forwards.
def palindromes(input_string):
    reversed_string = input_string[::-1]
    return input_string == reversed_string


while True:
    input_string = input('Please type in a palindrome: ')
    if not palindromes(input_string):
        print("that wasn't a palindrome")
    if palindromes(input_string):
        print(f'{input_string} is a palindrome!')
        break
