# Please write a function named same_chars, which takes one string and two integers as
# arguments. The integers refer to indexes within the string. The function should return
# True if the two characters at the indexes specified are the same. Otherwise, and
# especially if either of the indexes falls outside the scope of the string, the function returns
# False.
def same_chars(input_strings, x, y):
    if y >= len(input_strings) or x >= len(input_strings):
        return False
    if input_strings[x] == input_strings[y]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(same_chars("coder", 1, 10))