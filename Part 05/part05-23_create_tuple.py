# Please write a function named create_tuple(x: int, y: int, z: int),
# which takes three integers as its arguments, and creates and returns a tuple
# based on the following criteria:

# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments
def create_tuple(x: int, y: int, z: int):
    result = (min(x, y, z), max(x, y, z), x + y + z)
    return result


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
