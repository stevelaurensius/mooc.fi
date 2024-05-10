phone_book = {}
while True:
    user_input = int(input('command (1 search, 2 add, 3 quit):'))
    pass
    if user_input == 1:
        name_search = input('name: ')
        if name_search in phone_book:
            for number in phone_book[name_search]:
                print(number)
        else:
            print('no number')
    elif user_input == 2:
        name_add = input('name: ')
        phone_add = input('number: ')
        if name_add in phone_book:
            phone_book[name_add].append(phone_add)
        else:
            phone_book[name_add] = [phone_add]
        print('ok!')
    elif user_input == 3:
        print('quitting...')
        break
