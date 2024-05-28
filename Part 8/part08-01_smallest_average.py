def smallest_average(person1: dict, person2: dict, person3: dict):
    person = {'person1': person1, 'person2': person2, 'person3': person3}
    average = {}
    average['person1'] = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    average['person2']= (person2['result1'] + person2['result2'] + person2['result3']) / 3
    average['person3'] = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    smallest = min(average, key=average.get)
    return person[smallest]


if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Mary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Mary", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
