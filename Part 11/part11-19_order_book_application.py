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

    def mark_finished(self, id_: int):
        for item in self.order_book:
            if item.id == id_:
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
                if item.programmer == programmer and item.is_finished():
                    finished_task += 1
                elif item.programmer == programmer and not item.is_finished():
                    unfinished_task += 1

                if item.programmer == programmer and item.is_finished():
                    finished_time += item.workload
                elif item.programmer == programmer and not item.is_finished():
                    unfinished_time += item.workload

        if not programmer_found:
            print('erroneous input')

        return finished_task, unfinished_task, finished_time, unfinished_time


class OrderBookApplication:
    def __init__(self):
        self._order_book = OrderBook()

    def instructions(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')
        print()

    def app_add_order(self):
        description = input('description: ')
        user_input = input('programmer and workload estimate: ').split()
        if len(user_input) != 2:
            print('erroneous input')
            print()
        else:
            programmer, workload = user_input
            if not workload.isdigit():
                print('erroneous input')
                print()
            else:
                workload = int(workload)
                self._order_book.add_order(description, programmer, workload)
                print('added!')
                print()

    def app_finished_order(self):
        finished_order = self._order_book.finished_orders()
        if len(finished_order) == 0:
            print('no finished tasks')
        else:
            for order in finished_order:
                print(order)
        print()

    def app_unfinished_order(self):
        unfinished_order = self._order_book.unfinished_orders()
        if len(unfinished_order) == 0:
            print('no unfinished tasks')
        else:
            for order in unfinished_order:
                print(order)
        print()

    def app_mark_finished(self):
        id_available = []
        for item in self._order_book.all_orders():
            id_available.append(item.id)
        id_to_mark = input('id: ')
        if not id_to_mark.isdigit():
            print('erroneous input')
        else:
            id_to_mark = int(id_to_mark)
            if id_to_mark not in id_available:
                print('erroneous input')
                print()
            else:
                self._order_book.mark_finished(id_to_mark)
                print('marked as finished')
                print()

    def app_programmer(self):
        programmers = self._order_book.programmers()
        for programmer in programmers:
            print(programmer)
        print()

    def app_status_of_programmer(self):
        programmer_name = input('programmer: ')
        stats = self._order_book.status_of_programmer(programmer_name)
        print(f'tasks: finished {stats[0]} not finished {stats[1]}, hours: done {stats[2]} scheduled {stats[3]}')

    def execute(self):
        self.instructions()
        while True:
            user_input = int(input('command: '))
            if user_input == 0:
                break
            if user_input == 1:
                self.app_add_order()
            if user_input == 2:
                self.app_finished_order()
            if user_input == 3:
                self.app_unfinished_order()
            if user_input == 4:
                self.app_mark_finished()
            if user_input == 5:
                self.app_programmer()
            if user_input == 6:
                self.app_status_of_programmer()
                break
        return


orderbook = OrderBookApplication()
orderbook.execute()
