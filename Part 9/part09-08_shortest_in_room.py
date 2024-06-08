# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Student(name={self.name}, height={self.height})"


class Room:
    def __init__(self):
        self.person = []

    def add(self, person: Person):
        self.person.append(person)

    def is_empty(self):
        for person in self.person:
            return False
        else:
            return True

    def print_contents(self):
        result = len(self.person)
        combined_height = 0
        for i in self.person:
            combined_height += i.height
        print(f'There are {result} persons in the room, and their combined height is {combined_height} cm')
        for i in self.person:
            print(f'{i.name} ({i.height} cm)')

    def shortest(self):
        if self.is_empty() == True:
            return None
        else:
            shortest_student = min(self.person, key=lambda student: student.height)
            return shortest_student

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_student = self.shortest()
        if shortest_student:
            self.person.remove(shortest_student)
        return shortest_student


if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
