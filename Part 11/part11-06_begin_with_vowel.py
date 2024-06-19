def begin_with_vowel(words: list):
    return [item for item in words if item[0] in 'aiueoAIUEO']


if __name__ == '__main__':
    word_list = ["automobile", "motorbike", "Animal", "cat", "Dog", "APPLE", "orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
