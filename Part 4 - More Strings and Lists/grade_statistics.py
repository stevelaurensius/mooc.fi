import math


temp_container = []
int_container = []
point_container = []
point_average = 0
counter = 0
grade_0 = 0
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
grade_5 = 0


while True:
    user_input = input('Exam points and exercises completed: ')
    if user_input == '':
        break
    else:
        temp_container.append(user_input.split())


int_container = [[int(x) for x in sublist] for sublist in temp_container]


for _ in int_container:
    point_container.append([int_container[counter][0],(math.floor(int_container[counter][1]/10)),
                            (int_container[counter][0] + (math.floor(int_container[counter][1]/10)))])
    counter += 1


counter = 0
while counter < len(point_container):
    if point_container[counter][0] < 10:
        grade_0 += 1
    elif 0 <= point_container[counter][2] <= 14:
        grade_0 += 1
    elif 15 <= point_container[counter][2] <= 17:
        grade_1 += 1
    elif 18 <= point_container[counter][2] <= 20:
        grade_2 += 1
    elif 21 <= point_container[counter][2] <= 23:
        grade_3 += 1
    elif 24 <= point_container[counter][2] <= 27:
        grade_4 += 1
    elif 28 <= point_container[counter][2] <= 30:
        grade_5 += 1
    counter += 1


counter = 0
while counter < len(point_container):
    point_average += point_container[counter][2]
    counter += 1
point_average = point_average / len(point_container)


pass_percentage = (grade_1 + grade_2 + grade_3 + grade_4 + grade_5) / len(point_container) * 100


print('Statistics:')
print(f'Points average: {round(point_average, 1)}')
print(f'Pass percentage: {round(pass_percentage, 1)}')
print('Grade distribution:')
print(f'  5: {"*" * grade_5}')
print(f'  4: {"*" * grade_4}')
print(f'  3: {"*" * grade_3}')
print(f'  2: {"*" * grade_2}')
print(f'  1: {"*" * grade_1}')
print(f'  0: {"*" * grade_0}')
