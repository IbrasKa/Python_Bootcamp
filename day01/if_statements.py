
if False :
    print('Python Programming')

print('Java Programming')

print('-------------------------------------------------')

score = 78

if score >= 60 :
    print('Congrats! You passed the exam')

"""..."""

s = 'Hello World'

if 'H' and 'W' in s :
    print(s, 'has', 'H and W')

print('-------------------------------------------------')

if score >= 60 :
    print ('Passed')

else :
    print('Failed')

print('-------------------------------------------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else :
    result = 'Not eligible'

print(result)

print('-------------------------------------------------')

# Ternary :

age = 26
result = 'Eligible' if age >= 21 else 'Not eligible'
print(result)

print('-------------------------------------------------')

num = 100
result = None

if num > 0 :
    result = 'Positive'
elif num < 0:   # same with else if block Java
    result = 'Negative'
else:
    result = 'Zero'

print(result)
# Ternary can not be USED for multi-branch if-statement, it can only be used if-else statement

print('-------------------------------------------------')

num = 200

result2 = 'Positive' if num > 0 else 'Zero'

print(result2)

print('-------------------------------------------------')

score = -300
if 0 <= score <= 100:
    if score >= 60 :
        print('Passed')
    else:
        print('Failed')
else :
    print('Invalied score')

print('-------------------------------------------------')

"""
A score of a student is given, write a program that can calculate the grade of the student

"""

grade = 79

if 0 <= grade <= 100:

    if grade >=90:
        print ("Your grade is A")
    elif grade >=80:
        print("Your grade is B")
    elif grade >=70:
        print("Your grade is C")
    elif grade >=60:
        print("Your grade is D")
    else:
        print("Your grade is F")
else :
    print('Invalid grade')

