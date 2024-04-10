# Please write a function named greatest_number, which takes three arguments. The
# function returns the greatest in value of the three.
def greatest_number(x, y, z):
    return max(x, y, z)


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
