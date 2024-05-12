# Please write a function named largest, which reads the file and returns the largest
# number in the file.

# Notice that the function does not take any arguments. The file you are working with is
# always named numbers.txt.

def largest():
    with open('numbers.txt') as file:
        biggest_number = 0
        for number in file:
            number = int(number)
            if number > biggest_number:
                biggest_number = number
        return biggest_number
