class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, another):
        if f"{self._euros}.{self._cents:02d}" == f'{another._euros}.{another._cents:02d}':
            return True
        else:
            return False

    def __ne__(self, another):
        if f"{self._euros}.{self._cents:02d}" != f'{another._euros}.{another._cents:02d}':
            return True
        else:
            return False

    def __lt__(self, another):
        if f"{self._euros}.{self._cents:02d}" < f'{another._euros}.{another._cents:02d}':
            return True
        else:
            return False

    def __gt__(self, another):
        if f"{self._euros}.{self._cents:02d}" > f'{another._euros}.{another._cents:02d}':
            return True
        else:
            return False

    def __add__(self, another):
        total_euros = self._euros + another._euros
        total_cents = self._cents + another._cents
        if total_cents > 99:
            total_euros += 1
            total_cents = total_cents - 100
        total_money = Money(total_euros, total_cents)
        return total_money

    def __sub__(self, another):
        total_euros = self._euros - another._euros
        if self._cents < another._cents:
            total_euros -= 1
            self._cents += 100
            total_cents = self._cents - another._cents
        else:
            total_cents = self._cents - another._cents
        total_money = Money(total_euros, total_cents)

        if total_money._euros < 0:
            raise ValueError(f"a negative result is not allowed")
        else:
            return total_money


if __name__ == '__main__':
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    print(e1)
    e1.euros = 1000
    print(e1)
