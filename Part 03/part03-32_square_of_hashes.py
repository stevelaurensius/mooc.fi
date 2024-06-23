# Please write a function named hash_square(length), which takes an integer
# argument. The function prints out a square of hash characters, and the argument
# specifies the length of the side of the square.
def hash_square(times):
    i = 1
    while i <= times:
        print('#' * times)
        i += 1


if __name__ == "__main__":
    hash_square(5)
