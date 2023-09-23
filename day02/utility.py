import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')


def value():
    return 'Python Programming'


def square(num):
    return num * num


def return_int() -> int:
    return 10


def divide(num1, num2):
    return num1 / num2


def square2(num: int):  # You can indicate the type of passing argument
    return num * num


def add(num1: int, num2: int):  # to use float/int  wright NUMBERS
    return num1 + num2


def add1(num1: numbers, num2: numbers) -> int:
    return num1 + num2


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:  # ======> THIS IS FUNCTION
    return n1 + n2 + n3 + n4


class Test:
    def method(self):  # =========> THIS IS A METHOD. 1. CLASS ICINDE. 2. def'den once indentation bulunmakta.
        pass


def concat(a: str, b, c='', d='', e=''):
    print(f"{a} {b} {c} {d} {e}".strip())
