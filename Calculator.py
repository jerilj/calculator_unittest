def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplicaton(a, b):
    return a * b


def division(a, b):
    return a / b


def get_square_root(a):
    return a ** 0.5


class Calculator:
    def __init__(self):
        self.result = 0
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplicaton(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = multiplicaton(a, a)
        return self.result

    def square_root(self, a):
        self.result = get_square_root(a)
        return self.result
