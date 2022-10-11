"""
TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""


class CashRegister:

    def __init__(self):
        self.total_items = None  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item, price):
        if self.total_items is None:
            self.total_items = {}
        self.total_items[item] = price
        self.total_price += price

    def remove_item(self, item):
        print('--- Removing {}--- '.format(item))
        removed = self.total_items.pop(item)
        self.total_price -= removed

    def apply_discount(self, percentage):
        self.discount = percentage
        print('We will apply {}% discount'.format(self.discount))
        self.total_price *= (1 - self.discount / 100)

    def get_total(self):
        print('*** Total amount is : £{:.2f} ***\n'.format(self.total_price))

    def show_items(self):
        if self.total_items is None:
            print('Basket is empty.')
        else:
            print('***Here are your items***')
            for item, price in self.total_items.items():
                print(item, price)

    def reset_register(self):
        print('--- Resetting the register--- ')
        self.total_items = None  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:

CashRegister1 = CashRegister()

# ADD

CashRegister1.add_item('Apple', 1.00)
CashRegister1.add_item('Banana', 0.20)
CashRegister1.add_item('Cherry', 2.00)

CashRegister1.show_items()
CashRegister1.get_total()

# REMOVE
CashRegister1.remove_item('Apple')

CashRegister1.show_items()
CashRegister1.get_total()

# Apply Discount
CashRegister1.apply_discount(10)  # 10% discount of the total price

CashRegister1.get_total()

# Reset Register
CashRegister1.reset_register()

CashRegister1.show_items()
CashRegister1.get_total()
