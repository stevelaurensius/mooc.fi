class Item:
    def __init__(self, item_name: str, item_weight: int):
        self.__item_name = item_name
        self.__item_weight = item_weight

    def name(self):
        return self.__item_name

    def weight(self):
        return self.__item_weight

    def __str__(self):
        return f'{self.__item_name} ({self.__item_weight} kg)'


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcase_list = []
        self.__capacity = 0

    def add_item(self, items: Item):
        if items.weight() <= self.__max_weight - self.__capacity:
            self.__capacity += items.weight()
            self.__suitcase_list.append(items)
        else:
            pass

    def print_items(self):
        for item in self.__suitcase_list:
            print(item)

    def weight(self):
        total_weight = 0
        for i in self.__suitcase_list:
            total_weight += i.weight()
        return total_weight

    def heaviest_item(self):
        if len(self.__suitcase_list) == 0:
            return None
        else:
            heaviest_item = self.__suitcase_list[0]
            for i in self.__suitcase_list:
                if i.weight() >= heaviest_item.weight():
                    heaviest_item = i
            return heaviest_item

    def __str__(self):
        if len(self.__suitcase_list) == 1:
            units = 'item'
        elif len(self.__suitcase_list) != 1:
            units = 'items'
        return f'{len(self.__suitcase_list)} {units} ({self.__capacity} kg)'


class CargoHold:
    def __init__(self, maximum_weight):
        self.__maximum_weight = maximum_weight
        self.__cargo_list = []
        self.__capacity = 0

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() <= self.__maximum_weight - self.__capacity:
            self.__capacity += suitcase.weight()
            self.__cargo_list.append(suitcase)

    def __str__(self):
        cargo_weight = 0
        for i in self.__cargo_list:
            cargo_weight += i.weight()
        final_weight = self.__maximum_weight - self.__capacity
        if len(self.__cargo_list) == 1:
            units = 'suitcase'
        else:
            units = 'suitcases'
        return f'{len(self.__cargo_list)} {units}, space for {final_weight} kg'

    def print_items(self):
        for suitcase in self.__cargo_list:
            suitcase.print_items()


if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
