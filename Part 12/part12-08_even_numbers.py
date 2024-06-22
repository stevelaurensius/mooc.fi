def even_numbers(beginning: int, maximum: int):
    while beginning < maximum:
        if beginning % 2 == 0:
            yield beginning
        else:
            beginning += 1
            yield beginning
        beginning += 1


if __name__ == '__main__':
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
