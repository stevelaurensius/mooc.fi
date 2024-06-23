# The program should again ask the user for the names of the files. Then the program
# should process the files and print out a grade for each student.

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input('Exam points: ')

student_dict = {}
with open(student_info) as students:
    for line in students:
        line = line.replace('\n', '')
        line = line.split(';')
        if line[0] == 'id':
            continue
        student_dict[int(line[0])] = [line[1], line[2]]

exercise_dict = {}
with open(exercise_data) as exercises:
    for line in exercises:
        line = line.replace('\n', '')
        line = line.split(';')
        if line[0] == 'id':
            continue
        helper = [int(x) for x in line[1:]]
        exercise_dict[int(line[0])] = helper

exam_dicts = {}
with open(exam_points) as exams:
    for line in exams:
        line = line.replace('\n', '')
        line = line.split(';')
        if line[0] == 'id':
            continue
        helper = [int(x) for x in line[1:]]
        exam_dicts[int(line[0])] = helper

for id in student_dict:
    if 0 <= (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4)) <= 14:
        grade = 0
    elif 15 <= (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4)) <= 17:
        grade = 1
    elif 18 <= (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4)) <= 20:
        grade = 2
    elif 21 <= (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4)) <= 23:
        grade = 3
    elif 24 <= (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4)) <= 27:
        grade = 4
    else:
        grade = 5
    print(student_dict[id][0], student_dict[id][1], grade)
