from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(list_: list):
    return reduce(lambda x, y: x + y.credits, list_, 0)


def sum_of_passed_credits(attempts: list):
    passed_attempts = filter(lambda x: x.grade >= 1, attempts)
    return reduce(lambda total, attempt: total + attempt.credits, passed_attempts, 0)


def average(list_: list):
    passed_attempts = filter(lambda x: x.grade >= 1, list_)
    result = reduce(lambda total, attempt: total + attempt.grade, passed_attempts, 0)
    attemps = len(list(filter(lambda x: x.grade >= 1, list_)))
    return result / attemps


if __name__ == '__main__':
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
