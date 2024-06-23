# Please write a function named retrieve_course(course_name: str),
# which returns statistics for the specified course, in dictionary format.
import urllib.request
import json
import math


def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    result = []
    for course in courses:
        if course['enabled'] is True:
            exercise_data = (course['fullName'], course['name'], course['year'], sum(course['exercises']))
            result.append(exercise_data)
    return result


def retrieve_course(course_name: str):
    my_stat = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    stat = my_stat.read()
    stats = json.loads(stat)
    weeks = len(stats)
    answer = {}
    for course in course_name:
        students = max(course["students"] for course in stats.values())
        hours = sum(course["hour_total"] for course in stats.values())
        hours_average = math.floor(hours / students)
        exercises = sum(course["exercise_total"] for course in stats.values())
        exercises_average = math.floor(exercises / students)
        answer =  {'weeks': weeks, 'students': students, 'hours': hours, 'hours_average': hours_average,
                    'exercises': exercises, 'exercises_average': exercises_average}
    return answer


if __name__ == '__main__':
    print(retrieve_course("docker2019"))
