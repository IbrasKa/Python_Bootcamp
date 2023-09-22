"""

Java Methods
    public static void method (parameter
"""
import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')


display_message()


def value():
    return 'Python Programming'


print(value())


def square(num):
    return num * num


print(square(10))


def return_int() -> int:
    return 10


print(return_int())


def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


# print(divide('C#', 'Python'))


def square2(num: int):  # You can indicate the type of passing argument
    return num * num


print(square2(12))


# print(square2('Java'))

def add(num1: int, num2: int):  # to use float/int  wright NUMBERS
    return num1 + num2


print(add(10, 28))


def add1(num1: numbers, num2: numbers) -> int:
    return num1 + num2


print(add1(10.8, 25.78))

print('-------------------------------------------------')


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


print(calculate(23, 16, '+'))

print(calculate(100.5, 2.5, '/'))

print(calculate(768, 13, '%'))

print('-------------------------------------------------')


# THERE IS NO METHOD OVERLOADING. IN PYTHON WE CAN DO IT ONLY ONE METHOD

# example of method overloading in python
# def sum(n1: numbers, n2: numbers, n3: numbers, n4:numbers) ->numbers: # if
# I assign 2 arguments it gives ERROR. So we need to provide default value

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:  # ======> THIS IS FUNCTION
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(10, 20, 30))

print(sum(10, 20, 30, 40))


class Test:
    def method(self):  # =========> THIS IS A METHOD. 1. CLASS ICINDE. 2. def'den once indentation bulunmakta.
        pass


print('-------------------------------------------------')

# LET'S DO A FUNCTION COVERING ALL RULES FOR FUNCTION
# Concat Function'da ilk argumentimiz String olcak digerlerinin TYPE'i belirsiz

def concat (a: str, b, c= '', d= '', e= ''):
    print(f"{a} {b} {c} {d} {e}".strip())

concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)


"""
ABOUT THE FUNCTION
1. Declaring
2. Parameters
3. Restricting parameters' data type
4. Setting default value to parameters
5. Restricting return data type

Make sure you understand DYNAMIC TYPING
"""

