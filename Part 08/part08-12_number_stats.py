# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.number_list = []

    def add_number(self, number: int):
        self.number_list.append(number)

    def count_numbers(self):
        return len(self.number_list)

    def get_sum(self):
        return sum(self.number_list)

    def average(self):
        if self.count_numbers() == 0:
            return 0
        else:
            average_result = self.get_sum() / self.count_numbers()
            return average_result


stats = NumberStats()
even_number = NumberStats()
odd_number = NumberStats()
while True:
    user_input = int(input())
    if user_input != -1:
        stats.add_number(user_input)
        if user_input % 2 == 0:
            even_number.add_number(user_input)
        else:
            odd_number.add_number(user_input)
    else:
        print("Sum of numbers:", stats.get_sum())
        print("Mean of numbers:", stats.average())
        print(f'Sum of even numbers: {even_number.get_sum()}')
        print(f'Sum of odd numbers: {odd_number.get_sum()}')
        break
