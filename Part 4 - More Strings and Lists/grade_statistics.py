dict_container = []
student_point = []


def user_input_func():
    dict_container_int = []
    while True:
        user_input = input('Exam points and exercises completed: ')
        if user_input == '':
            break
        else:
            dict_container.append(user_input.split())
    dict_container_int = [[int(x) for x in sublist] for sublist in dict_container]
    # dict_container_int = [[15, 87], [10, 55], [11, 40], [4, 17]]
    return dict_container_int


def exercise_converter():
    dict_container_int = user_input_func()
    dict_point = [[sublist[0], sublist[1], sublist[0] + int(sublist[1] / 10)] for sublist in dict_container_int]
    return dict_point


def grade_converter():
    dict_point2 = exercise_converter()
    index_helper = 0
    while index_helper < len(dict_point2):
        if dict_point2[index_helper][2] < 10:
            dict_point2[index_helper].append(0)
        elif 0 <= dict_point2[index_helper][2] <= 14:
            dict_point2[index_helper].append(0)
        elif 15 <= dict_point2[index_helper][2] <= 17:
            dict_point2[index_helper].append(1)
        elif 18 <= dict_point2[index_helper][2] <= 20:
            dict_point2[index_helper].append(2)
        elif 21 <= dict_point2[index_helper][2] <= 23:
            dict_point2[index_helper].append(3)
        elif 24 <= dict_point2[index_helper][2] <= 27:
            dict_point2[index_helper].append(4)
        elif 28 <= dict_point2[index_helper][2] <= 30:
            dict_point2[index_helper].append(5)
        index_helper += 1
    return dict_point2


# def statistics():
#     dict_point4 = grade_converter()
#     # [[15, 87, 23, 3], [10, 55, 15, 1], [11, 40, 15, 1], [4, 17, 5, 0]]
#     average = 0
#     another_counter = 0
#     print('Statistics:')
#
#     i = 0
#     while i < len(dict_point4):
#         average += dict_point4[i][2]
#         i += 1
#     print(f'Points average: {average / 4}')
#
#     i = 0
#     while i < len(dict_point4):
#         if dict_point4[i][3] > 0:
#             another_counter += 1
#             i += 1
#         else:
#             i += 1
#     print(f'Pass percentage: {another_counter / len(dict_point4) * 100}')


def grade_counter(x):
    dict_point3 = grade_converter()
    i = 0
    point_counter = 0
    while i < len(dict_point3[0]):
        if dict_point3[i][3] == x:
            point_counter += 1
            i += 1
        else:
            i += 1
    return point_counter * '*'


print(f'  5: {grade_counter(5)}')
print(f'  4: {grade_counter(4)}')
print(f'  3: {grade_counter(3)}')
print(f'  2: {grade_counter(2)}')
print(f'  1: {grade_counter(1)}')
print(f'  0: {grade_counter(0)}')
