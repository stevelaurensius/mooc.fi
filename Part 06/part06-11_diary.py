# Please write a program which works as a simply diary. The diary entries should be saved
# in the file diary.txt. When the program is executed, it should first read any entries
# already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. If you want to
# keep its contents, first make a copy of the file under a different name.

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    option = int(input('Function: '))
    if option == 1:
        diary_text = input('Diary entry: ')
        with open('diary.txt', 'a') as diary:
            diary.write(f'{diary_text}\n')
        print('Diary saved')
        pass
    if option == 2:
        print('Entries:')
        with open('diary.txt') as diary:
            for line in diary:
                line = line.replace('\n', '')
                print(line)
        pass
    if option == 0:
        print('Bye now!')
        break
