# Please write a function named oldest_person(people: list), which takes
# a list of tuples as its argument. In each tuple, the first element is the name of a
# person, and the second element is their year of birth. The function should find
# the oldest person on the list and return their name.


def oldest_person(people: list):
    for i in people:
        if i[1] == min([x[1] for x in people]):
            return i[0]
