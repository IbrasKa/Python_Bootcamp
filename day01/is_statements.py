
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
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)
# Ternary can not be USED for multi-branch if-statement, it can only be used if-else statement

print('-------------------------------------------------')

score = -300
if 0 <= score <= 100:
    if score >= 60 :
        print('Passed')
    else:
        print('Failed')
else :
    print('Invalied score')