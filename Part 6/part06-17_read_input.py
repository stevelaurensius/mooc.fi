def read_input(message: str, lower_number: int, upper_number: int):
    while True:
        try:
            user_input = input(message)
            number = int(user_input)
            if lower_number <= number <= upper_number:
                return number
            else:
                raise ValueError
        except ValueError:
            print(f'You must type in an integer between {lower_number} and {upper_number}')


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
