class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.second = second
        self.minute = minute
        self.hour = hour

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def set(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self.second = 0

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
