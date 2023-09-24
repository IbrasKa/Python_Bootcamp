"""
2. Create a python file named numbers, Write a program that asks user to enter
number for 5 times, and print how many positive and negative numbers user entered
            Ex:
                Inputs:
                    10
                    20
                    -1
                    0
                    3

                Output:
                    3 positive and 1 negative

"""


def positiveOrNegative():
    count_Positive = 0
    count_Negative = 0
    count_Zero = 0
    for x in range(0, 5):
        num = int(input('Please enter a number:\n'))
        if num > 0:
            count_Positive += 1
        elif num < 0:
            count_Negative += 1
        else:
            count_Zero += 1
    print(f'{count_Positive} times positive, {count_Negative} times negative, {count_Zero} times Zero')


positiveOrNegative()
