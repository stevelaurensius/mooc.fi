print('Person 1:')
person1_name = str(input('Name:'))
person1_age = int(input('Age:'))
print('Person 2:')
person2_name = str(input('Name:'))
person2_age = int(input('Age:'))

if person1_age > person2_age:
    print(f'The elder is {person1_name}')
elif person2_age > person1_age:
    print(f'The elder is {person2_name}')
else:
    print(f'{person1_name} and {person2_name} are the same age')
    