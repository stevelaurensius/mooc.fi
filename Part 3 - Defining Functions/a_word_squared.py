# Please write a function named squared, which takes a string argument and an
# integer argument, and prints out a square of characters

def squared(input_string, input_integer):
    text = input_string * int((input_integer * input_integer))
    i = 0
    j = input_integer
    counter = 1
    while counter <= input_integer:
        print(text[i:j])
        i += input_integer
        j += input_integer
        counter += 1


if __name__ == "__main__":
    squared()
