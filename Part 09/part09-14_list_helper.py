from collections import Counter


class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequency = Counter(my_list).most_common(1)
        return frequency[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        frequency = Counter(my_list)
        count_keys = sum(1 for value in frequency.values() if value >= 2)
        return count_keys


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
