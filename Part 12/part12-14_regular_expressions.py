import re


def is_dotw(my_string: str):
    my_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day in my_list:
        if re.search(day, my_string):
            return True
    return False


def all_vowels(my_string: str):
    pattern = r'^[aeiouAEIOU]+$'
    if re.fullmatch(pattern, my_string):
        return True
    return False


def time_of_day(my_string: str) -> bool:
    pattern = r'^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    if re.fullmatch(pattern, my_string):
        return True
    return False


if __name__ == '__main__':
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
