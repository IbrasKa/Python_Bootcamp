"""
3. Create a python file named sum_of_even_odd:
        3.1 Write a program that can return the sum of even numbers between 1 to 100

        3.2 Write a program that can return the sum of odd numbers between 1 to 100

        3.3 write a program that can calculate the sum of all numbers between 1 to any given number
            ex:
                input: 100
                output: 5050

                input: 50
                output: 1275
"""


def sumOfEvenOdd(num: int = 0):
    sumEven = 0
    sumOdd = 0
    sumAll = 0
    for x in range(1, num + 1):
        sumAll += x
        if x % 2 != 0:
            sumOdd += x
        else:
            sumEven += x
    print(f"Summ of all numbers 1 to {num} = {sumAll}\n"
          f"Summ of odd numbers 1 to {num} = {sumOdd}\n"
          f"Summ of odd numbers 1 to {num} = {sumEven}")


sumOfEvenOdd(50)
