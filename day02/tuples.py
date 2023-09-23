

days = ('Monday', 'Tuesday', "Wednesday", 'Thursday', "Friday", "Saturday", 'Sunday', 1, 2, 3, 4, 5, 6, 7, True, False)


print(type(days))
print(len(days))

print(days)

# days[0] = 'Java' # TUPLE does not UPDATE the value
# print(days)

print(days[0])
print(days[-1])
print(days[::-1])


# SLICING TUPLE
days = ('Monday', 'Tuesday', "Wednesday", 'Thursday', "Friday", "Saturday", 'Sunday')

work_days = days[1:4]
# work_days = days[1:-3] # Yukaridaki ile ayni
print(work_days)

# Monday to Friday
week_days = days[:-2]
print(week_days)

# Last three elements
weekend = days[-3:]
print(weekend)

# ==, is

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

# Verifying these 2 tuples are equal
print(tuple1 == tuple2)

# Verifying element is in tuples are the same object
print(tuple1 is tuple2)

# merging two tuples
tuple3 = tuple1 + tuple2
print(tuple3)

# multiplying tuples
tuple4 = tuple1 * 5
print(tuple4)

# reversing tuple
reversed_tuple1 = days[::-1]
print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

# reversing with loops
for day in days[::-1]:
    print(day)

for num in tuple(reversed(tuple1)):
    print(num,end=" ",)


print('\n-------------------------------------------------')
# printing index no
print(days.index('Wednesday'))

# to get the reversed index number

for x in reversed(range(0, len(days))):
    print(x, end=" ")

print('\n-------------------------------------------------')

nested_tuple = ( (1, 2, 3, ), (4, 5, 6, 7, 8), (9, 10))
print(len(nested_tuple))

# we can iterate nested tupe with nested loop

print('\n-------------------------------------------------')

for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

print('\n-------------------------------------------------')

for i in range(0, len(nested_tuple)):
    for j in range (0,len(nested_tuple[i])):
        print(nested_tuple[i][j])
