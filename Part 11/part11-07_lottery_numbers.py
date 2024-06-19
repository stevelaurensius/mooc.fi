class LotteryNumbers:
    def __init__(self, week: int, correct_number: list):
        self.week = week
        self.correct_number = correct_number

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.correct_number])

    def hits_in_place(self, numbers):
        return [number if number in self.correct_number else -1 for number in numbers]


if __name__ == '__main__':
    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]

    print(week8.hits_in_place(my_numbers))
