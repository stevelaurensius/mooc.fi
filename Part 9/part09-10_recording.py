class Recording:
    def __init__(self, user_input: int):
        if user_input > 0:
            self.__length = user_input
        else:
            raise ValueError("The amount must not be below zero")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, user_update: int):
        if user_update > 0:
            self.__length = user_update
        else:
            raise ValueError("The amount must not be below zero")


if __name__ == '__main__':
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
