"""
4. Create a python file named factorial_number, Write a program that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120

                    ( because: 5! = 5 * 4 * 3 * 2* 1 = 120 )
"""


def factorialNumbers(num: int):
    result = 1
    if num > 0:
        for x in range(1, num + 1):
            result *= x
    elif num < 0:
        for x in range(num, 0):
            result *= x
    print(result)


factorialNumbers(0)