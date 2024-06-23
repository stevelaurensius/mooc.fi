# Please write a function named print_persons(filename: str), which
# reads a JSON file in the above format, and prints the contents.
# The file may contain any number of entries.
import json


def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    courses = json.loads(data)

    for course in courses:
        hobbies = f"({', '.join(course['hobbies'])})"
        print(course['name'], course['age'], 'years', hobbies)
