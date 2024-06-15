class SimpleDate:
    def __init__(self, date, month, year):
        self._date = date
        self._month = month
        self._year = year

    def __str__(self):
        return f'{self._date}.{self._month}.{self._year}'

    @property
    def get_time(self):
        return f'{self._date}.{self._month}.{self._year}'

    @property
    def get_date(self):
        return self._date

    @property
    def get_month(self):
        return self._month

    @property
    def get_year(self):
        return self._year

    def __eq__(self, another):
        if self.get_time == another.get_time:
            return True
        else:
            return False

    def __ne__(self, another):
        if self.get_time != another.get_time:
            return True
        else:
            return False

    def __lt__(self, another):
        if self.get_year < another.get_year:
            return True
        elif self.get_year > another.get_year:
            return False
        else:
            if self.get_month < another.get_month:
                return True
            elif self.get_month > another.get_month:
                return False
            else:
                if self.get_date < another.get_date:
                    return True
                else:
                    return False

    def __gt__(self, another):
        if self.get_year > another.get_year:
            return True
        elif self.get_year < another.get_year:
            return False
        else:
            if self.get_month > another.get_month:
                return True
            elif self.get_month < another.get_month:
                return False
            else:
                if self.get_date > another.get_date:
                    return True
                else:
                    return False

    def __add__(self, value):
        new_date = self.get_date
        new_month = self.get_month
        new_year = self.get_year

        if (new_date + value) < 30:
            new_date += value
        else:
            new_date += value % 30
            if new_date > 30:
                new_month += 1
                new_date -= 30
            else:
                new_date = new_date
            new_month += value // 30
            if new_month > 12:
                new_year += new_month // 12
                new_month = new_month % 12

        result = SimpleDate(new_date, new_month, new_year)
        return result

    def __sub__(self, another):
        days_self = self._to_days()
        days_another = another._to_days()
        return abs(days_self - days_another)

    def _to_days(self):
        return self._date + self._month * 30 + self._year * 360


if __name__ == '__main__':
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
