# Please write a program which asks the user to type in a sentence. The program then
# prints out the first letter of each word in the sentence, each letter on a separate line.

input_string = input('Please type in a sentence: ')
dictionary = input_string.split()

for i in range(len(dictionary)):
    print(dictionary[i][0])
    i += 1
