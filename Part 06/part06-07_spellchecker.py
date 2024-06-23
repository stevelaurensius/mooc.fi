if True:
    text_input = input(('Write text: '))
else:
    text_input = 'We use ptython to make a spell checker'

result = []
text_input = text_input.split(' ')
for word in text_input:
    with open('wordlist.txt') as wordlist:
        found = False
        for correct_word in wordlist:
            correct_word = correct_word.replace('\n', '')
            if word.lower() == correct_word:
                result.append(word)
                found = True
                break
    if found == False:
        result.append(f'*{word}*')
print(' '.join(result))
