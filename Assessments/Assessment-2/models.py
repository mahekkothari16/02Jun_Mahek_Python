class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Customer(Person):
    def __init__(self, name, phone, balance):
        super().__init__(name, phone)
        self.__balance = balance  # Private field

    def get_balance(self):
        return self.__balance

    def update_balance(self, amount):
        self.__balance += amount


class Product:
    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = price
        self.qty = qty

    def get_total(self):
        return self.price * self.qty
