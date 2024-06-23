from datetime import datetime


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    else:
        pass
    control_list = list('0123456789ABCDEFHJKLMNPRSTUVWXY')
    century_marker = ['+', '-', 'A']

    if pic[6] == '+':
        full_year = int(pic[4:6]) + 1800
    elif pic[6] == '-':
        full_year = int(pic[4:6]) + 1900
    elif pic[6] == 'A':
        full_year = int(pic[4:6]) + 2000
    try:
        birth_date = datetime(full_year, int(pic[2:4]), int(pic[0:2]))
    except:
        return False
    if pic[0] != 0:
        nine_digits = int(pic[0:6] + pic[7:10]) % 31
    else:
        nine_digits = int(pic[1:6] + pic[7:10]) % 31

    if (pic[6] in century_marker) and (pic[10] == control_list[nine_digits]):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_it_valid('081842-720N'))
