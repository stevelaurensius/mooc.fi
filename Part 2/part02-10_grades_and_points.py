point = int(input('How many points [0-100]:'))
if point < 0:
    print('impossible!')
elif 0 <= point <= 49:
    print('fail')
elif 50 <= point <= 59:
    print('Grade: 1')
elif 60 <= point <= 69:
    print('Grade: 2')
elif 70 <= point <= 79:
    print('Grade: 3')
elif 80 <= point <= 89:
    print('Grade: 4')
elif 90 <= point <= 100:
    print('Grade: 5')
else:
    print('impossible!')
    