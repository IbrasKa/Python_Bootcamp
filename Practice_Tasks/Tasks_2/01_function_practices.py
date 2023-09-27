"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""
import numbers


def eligibleToVote(age: int = 0, country: str = ''):
    if 18 <= age <= 150:
        if country.lower() == 'usa':
            print('You are eligible to vote!')
        else:
            print('Ineligible to vote')
    else:
        print('Ineligible to vote')


eligibleToVote(28, 'USA')


def gradeOfStudent(grade: numbers = 0):
    if 'A' <= grade.upper() <= 'F':
        if grade.upper() == 'A':
            print('Excellent')
        elif grade.upper() == 'B':
            print('Great job')
        elif grade.upper() == 'C':
            print('Good')
        elif grade.upper() == 'D':
            print('Passed')
        elif grade.upper() == 'F':
            print('Failed')
    else:
        print('Invalid Grade')


gradeOfStudent('z')


def positiveNegativeNumber(num: int = 0):
    if type(num) == int:
        if num > 0:
            print('Positive Number')
        elif num < 0:
            print('Negative number')
        else:
            print('It is Zero')
    else:
        print(f'Type of argument is {type(num).__name__}. It is invalid')


positiveNegativeNumber(30)


def isPalindrome(words: str = ''):
    if type(words) == str:
        if words.lower() == words.lower()[::-1]:
            return True
        else:
            return False
    else:
        return 'Invalid'


print(isPalindrome('Ey Edip Adanada Pide Ye'))
