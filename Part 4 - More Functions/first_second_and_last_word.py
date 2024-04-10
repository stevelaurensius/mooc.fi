# Please write three functions: first_word, second_word and last_word. Each
# function takes a string argument.

# As their names imply, the functions return either the first, the second or the last word in
# the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two separate words, and all words
# are separated by exactly one space character. There will be no spaces in the beginning or at the end of the
# argument strings.

def first_word(x):
    x_index = x.split()
    return x_index[0]


def second_word(y):
    y_index = y.split()
    return y_index[1]


def last_word(z):
    z_index = z.split()
    return z_index[-1]


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
