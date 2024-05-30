class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        lunch_price = 2.60
        if self.balance > lunch_price:
            self.balance -= lunch_price
        else:
            self.balance = self.balance

    def eat_special(self):
        special_price = 4.60
        if self.balance > special_price:
            self.balance -= special_price
        else:
            self.balance = self.balance

    def deposit_money(self, deposit):
        if deposit <= 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        else:
            self.balance += deposit

    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'


peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.deposit_money(20)
graces_card.eat_special()
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print(f'Peter: {peters_card}')
print(f'Grace: {graces_card}')
