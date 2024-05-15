# Please write a program which asks the user for the names of these two files, reads the
# files, and then prints out the total number of exercises completed by each student. If the
# files have the contents in the examples above, the program should print out the following:

# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

for id in student_dict:
    print(student_dict[id][0], student_dict[id][1], sum(exercise_dict[id]))
