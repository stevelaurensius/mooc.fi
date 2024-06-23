dict_file = 'dictionary.txt'


while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    user_option = int(input('Function: '))
    if user_option == 3:
        print('Bye!')
        break
    elif user_option == 1:
        finnish_input = input('The word in Finnish: ')
        english_input = input('The word in English: ')
        with open(dict_file, 'a') as dictionary:
            dictionary_input = finnish_input + ';' + english_input + '\n'
            dictionary.write(dictionary_input)
        print('Dictionary entry added')
    elif user_option == 2:
        search_input = str(input('Search term: '))
        with open(dict_file, 'r') as dictionary:
            for line in dictionary:
                line = line.replace('\n', '')
                if search_input in line:
                    line = line.replace(';', ' - ')
                    print(line)
