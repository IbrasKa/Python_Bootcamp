"""
6. Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
             Ex:
                 input: A1B2C3

                 output: 6

"""


def sumOfDigits(words: str = ''):
    sumDigits = 0
    for i in range(0, len(words)):
        if words[i].isdigit():
            sumDigits += int(words[i])
    print(sumDigits)


sumOfDigits('ajbasjd9   49lKMS1`130DSAKdd012rknasdv=12-=131pp#f')
