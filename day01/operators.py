#arithmetic : +, -, *, /, %

print(10 - 2)
print(10 + 2)

print(10 * 3)

print(10/3) #DIVISION operator always give us FLOAT.

print(10/5)

print(10 % 3)

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100

a = 200 #Python always work from BOTTOM to TOP

print(a)

a += 100
print(a)

a /= 2
print(a)

# logical operators : and, or, not
s = 'Hello World'

print('H' and 'W' in s)

print(True and True)
print(True or True)

s = 'Java Python C# C++'
print('Java' or 'Ruby' in s)

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'
print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(False)

print('-------------------------------------------------')

s = 'Jave'
s2 = 'Jave'

print(s is s2) # to check if two variables are referencing to the same objetcs ( == operator of java)
