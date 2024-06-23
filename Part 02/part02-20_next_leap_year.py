year_input = int(input('Year'))
year = year_input + 1
leap_year = int(0)

while True:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap_year = year
            break
        if year % 100 != 0 and year % 400 != 0:
            leap_year = year
            break
    year += 1
print(f'The next leap year after {year_input} is {leap_year}')
