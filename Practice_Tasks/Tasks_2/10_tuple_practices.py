"""
10. Create a python file named tuples_practices:
        10.1 Write a program that can display the palindrome strings from a tuple of string

                Ex:
                    words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

                    output:
                        Anna
                        Level

"""
words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')


def palindrome_tuple(tuples):
    for x in tuples:
        if x == x[::-1].capitalize():
            print(x)


palindrome_tuple(words)

"""
10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5
"""
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)


def common_elements(a, b):
    for x in a:
        for y in b:
            if x == y:
                print(x)


common_elements(tuple1, tuple2)

"""
10.3 Write a program that can count the even and odd number from a tuple of integers
                
                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers
"""

numbers = (1, 2, 3, 4, 5, 6, 7)
def count_even_and_odd_numbers (nums : tuple = ()):
    countOdd = 0
    countEven = 0

    for x in nums:
        if x % 2 == 0:
            countOdd += 1
        else:
            countEven += 1

    print(f"There are {countOdd} even numbers and {countEven} odd numbers")


count_even_and_odd_numbers(numbers)