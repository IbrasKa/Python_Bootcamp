"""
Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade = 'a'

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
    print('Invalid')
