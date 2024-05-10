# Please write a function named chessboard, which prints out a chessboard made out
# of ones and zeroes. The function takes an integer argument, which specifies the
# length of the side of the board.
def chessboard(number):
    start_one = '10' * (number // 2) + '10'[:(number % 2)]
    start_zero = '01' * (number // 2) + '01'[:(number % 2)]
    counter = 1
    while True:
        if counter <= number:
            print(start_one)
            counter += 1
            pass
        if counter <= number:
            print(start_zero)
            counter += 1
        else:
            break


if __name__ == "__main__":
    chessboard(3)
