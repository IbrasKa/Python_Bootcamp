import numbers

"""
8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"
"""


def grade_calculator():
    score = float(input('Enter your score:\n'))
    if 0 <= score <= 100:
        if score >= 90:
            print('A')
        elif score >= 80:
            print('B')
        elif score >= 70:
            print('C')
        elif score >= 60:
            print('D')
        else:
            print('F')
    else:
        print('Invalid Entry')

    continueOrStop = input('Would you like to continue (Yes or No):\n')
    while not (continueOrStop.lower() == 'yes' or continueOrStop.lower() == 'no'):
        print("Please enter 'Yes' or 'No'\n")
        continueOrStop = input('Would you like to continue (Yes or No):\n')
    if continueOrStop.lower() == 'yes':
        grade_calculator()
    else:
        print('Thank you for using Cydeo Grade Calculator APP')


grade_calculator()
