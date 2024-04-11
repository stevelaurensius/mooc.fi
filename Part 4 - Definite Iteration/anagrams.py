# Please write a function named anagrams, which takes two strings as arguments.
# The function returns True if the strings are anagrams of each other. Two words
# are anagrams if they contain exactly the same characters.
# Some examples of how the function should work:
# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False
def anagrams(x, y):
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    return sorted_x == sorted_y


if __name__ == "__main__":
    print(anagrams())
