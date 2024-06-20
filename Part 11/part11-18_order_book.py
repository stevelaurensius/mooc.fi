class Task:
    unique_id = 0

    def __init__(self, description, programmer, workload):
        self._description = description
        self._programmer = programmer
        self._workload = workload
        self._id = Task.unique_id + 1
        self._status = False
        Task.unique_id += 1

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def programmer(self):
        return self._programmer

    @property
    def workload(self):
        return self._workload

    def is_finished(self):
        return self._status

    def mark_finished(self):
        self._status = True

    def __str__(self):
        result = 'NOT FINISHED' if self.is_finished() is False else 'FINISHED'
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {result}'


class OrderBook:
    def __init__(self):
        self.order_book = []

    def add_order(self, description, programmer, workload):
        self.order_book.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.order_book

    def programmers(self):
        programmers = []
        for order in self.order_book:
            if order.programmer not in programmers:
                programmers.append(order.programmer)
        return programmers

    def mark_finished(self, id: int):
        for item in self.order_book:
            if item.id == id:
                item.mark_finished()
                return
        raise ValueError('id not found')

    def finished_orders(self):
        result = []
        for item in self.order_book:
            if item.is_finished():
                result.append(item)
        return result

    def unfinished_orders(self):
        result = []
        for item in self.order_book:
            if not item.is_finished():
                result.append(item)
        return result

    def status_of_programmer(self, programmer: str):
        finished_task = 0
        unfinished_task = 0
        finished_time = 0
        unfinished_time = 0
        programmer_found = False
        for item in self.order_book:
            if item.programmer == programmer:
                programmer_found = True
                if item.programmer == programmer and item.is_finished() == True:
                    finished_task += 1
                elif item.programmer == programmer and item.is_finished() == False:
                    unfinished_task += 1

                if item.programmer == programmer and item.is_finished() == True:
                    finished_time += item.workload
                elif item.programmer == programmer and item.is_finished() == False:
                    unfinished_time += item.workload

        if not programmer_found:
            raise ValueError('Error')

        return finished_task, unfinished_task, finished_time, unfinished_time


if __name__ == '__main__':
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
