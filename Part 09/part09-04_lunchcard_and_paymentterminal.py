class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        lunch_price = 2.50
        if payment >= lunch_price:
            result = payment - lunch_price
            self.funds += lunch_price
            self.lunches += 1
        else:
            result = payment
        return result

    def eat_special(self, payment: float):
        lunch_price = 4.30
        if payment >= lunch_price:
            result = payment - lunch_price
            self.funds += lunch_price
            self.specials += 1
        else:
            result = payment
        return result

    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_price = 2.50
        if card.balance >= lunch_price:
            card.balance -= lunch_price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        lunch_price = 4.30
        if card.balance >= lunch_price:
            card.balance -= lunch_price
            self.specials += 1
            return True
        else:
            return False


    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += amount
        pass


if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
