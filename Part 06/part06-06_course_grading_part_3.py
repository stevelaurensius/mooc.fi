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

label_name = 'name'
label_exec_nbr = 'exec_nbr'
label_exec_pts = 'exec_pts.'
label_exm_pts = 'exm_pts.'
label_tot_pts = 'tot_pts.'
label_grade = 'grade'
print(f'{label_name:30}{label_exec_nbr:10}{label_exec_pts:10}{label_exm_pts:10}{label_tot_pts:10}{label_grade}')

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
    value_std_name = student_dict[id][0] + " " + student_dict[id][1]
    value_exec_nbr = sum(exercise_dict[id])
    value_exec_pts = sum(exercise_dict[id]) // 4
    value_exm_pts = sum(exam_dicts[id])
    value_tot_pts = (sum(exam_dicts[id]) + (sum(exercise_dict[id]) // 4))
    print(f'{value_std_name:30}{value_exec_nbr:<10}{value_exec_pts:<10}{value_exm_pts:<10}{value_tot_pts:<10}{grade}')
