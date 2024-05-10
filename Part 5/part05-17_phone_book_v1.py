phone_book = {}
while True:
    user_input = input('command (1 search, 2 add, 3 quit):')
    pass
    if user_input == '1':
        name_search = input('name: ')
        if name_search in phone_book:
            print(phone_book[name_search])
        else:
            print('no number')
    elif user_input == '2':
        name_add = input('name: ')
        phone_add = input('number: ')
        phone_book[name_add] = phone_add
        print('ok!')
    elif user_input == '3':
        print('quitting...')
        break
