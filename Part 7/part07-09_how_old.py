# Please write a program which asks the user for their date of birth, and then prints out
# how old the user was on the eve of the new millennium. The program should ask for the
# day, month and year separately, and print out the age in days. Please have a look at the
# examples below:
from datetime import datetime, timedelta

day_input = int(input('Day: '))
month_input = int(input('Month: '))
year_input = int(input('Year: '))


user_date_input = datetime(year_input, month_input, day_input)
new_millennium = datetime(1999, 12, 31)
difference = new_millennium - user_date_input
if difference.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f'You were {difference.days} days old on the eve of the new millennium.')
