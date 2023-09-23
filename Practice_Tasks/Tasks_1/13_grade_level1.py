
"""
Create a python file named grade_level1.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

              Assume that the given number is 1 ~ 18
"""

num = int (input('Enter a level number (1~18):\n'))

if 18>= num >= 1 :
    if num <=5:
        print('Your school type is Elementary School')
    elif num <=8:
        print('Your school type is Middle School')
    elif num <= 12:
        print('Your school type is High School')
    elif num <= 16:
        print('Your school type is College')
    else:
        print('Your school type is Grad School')
else :
    print('Invalid level number. Please try again')
