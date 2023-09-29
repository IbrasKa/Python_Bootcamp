groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')  # append() method is used for inserting 1 element to list

groceries_list.extend(('Beef', 'Oranges', 'Onion'))  # to add multiple element to list we are using extend() method.
#  elements should be in the TUPLE
print(len(groceries_list))
print(groceries_list)

# If I want to update 'Orange' to 'Cheery'

groceries_list[-2] = 'Cherry'

print(groceries_list)

print('-------------------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

# This time, I would like to update 4 elements at the same time (30, 40, 50, 60)

numbers_list[2:-2] = [300, 4000, 5, 60_000]

print(numbers_list)

print('-------------------------------------------------')

# Can I do slicing?

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(characters)

# I get those elements 'c', 'd', 'e', 'f' (son index'i hard copy kullanmadan yapalim. Normalde [2:-3] yazabilirdik

list1 = characters[2:len(characters) - 3]

print(list1)

# Slicing'i ilk indexten baslatiyorsak ilk indexi kullanmaya gerek yok. Bu defa a,b,c,d'yi alalim

list2 = characters[:4]

print(list2)

# What if I get from 3rd element to end of the list

list3 = characters[2:]

print(list3)

# If you want to update a range of elements and if you want to add more elements than range:

characters[2:5] = ['C', 'D', 'E', 'F', 'G', 'H', 'P']

# according to range of index,  relevant elements will be updated and the rest of the element will be added after update

print(characters)

print('-------------------------------------------------')

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

print('-------------------------------------------------')

# What if I update the element of list by using loop

nums = [10, 20, 30, 40, 50, 60]

# I want you to update the list element by dividing them to 5

for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)
print(nums)

print('-------------------------------------------------')

# let me get reversed list.
nums2 = [70, 80, 90, 100, 110, 120]

for y in reversed(range(len(nums2))):
    print(nums2[y])

print('-------------------------------------------------')

for x in nums2[::-1]:
    print(x)

print('-------------------------------------------------')

for z in reversed(nums2):
    print(z)

print('-------------------------------------------------')

# while loops takes only a condition and it will continue iteration until the condition is FALSE

nums3 = [100, 200, 300, 400, 500, 600]

i = 0

while len(nums3) > i:
    print(nums3[i])
    i += 1

# WHILE loop is never recommended for any of LIST, TUPLE, SET AND DICTIONARY.

print('-------------------------------------------------')

# Some unique methods for LIST
"""
Python List append() : Add a single element to the end of the list

Python List clear() : Removes all Items from the List

Python List copy() : returns a shallow copy of the list

Python List count() : returns count of the element in the list

Python List extend() : adds iterable elements to the end of the list

Python List index() : returns the index of the element in the list

Python List insert() : insert an element to the list

Python List pop() : Removes element at the given index

Python List remove() : Removes item from the list

Python List reverse() : reverses the list

Python List sort() : sorts elements of a list
"""

print('-------------------------------------------------')

nums4 = [60, 500, 10, 20, 15, 5, 0]

# nums4.sort()      # ascending order.

# if you want descending order :

nums4.sort(reverse=True)

print('-------------------------------------------------')

list4 = [10, 20, 30, 40]

# list4 = list(reversed(list4))

list4.reverse()

print(list4)

print('-------------------------------------------------')

# converting one data structure to another

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list5 = list(tuple_elements)

list5[-2] = 'C++'
list5.append('SWIFT')

print(list5)

tuple_elements = tuple(list5)

print(tuple_elements)

print('-------------------------------------------------')

list6 = [1, 2, 3, 4, 5, 6]
list7 = [1, 2, 3, 4, 5, 6]

print(list6 is list7)  # False. Because list is mutable, there is no guarantee that they will not be changed
# 'is' means REFERENCING

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (1, 2, 3, 4, 5, 6)

print(tuple1 is tuple2)  # True. Because tuple is immutable

print('-------------------------------------------------')

# remove () method

groceries_list.remove('Beef')
print(groceries_list)

# if you want to remove elements by index, we will use pop() method

groceries_list.pop(3)

print(groceries_list)

# If you don't put any index number, pop() removes last index

groceries_list.pop()  # will remove 'Onion'

print(groceries_list)

# What is the difference between append() and insert()?. in insert() method we will add an element with an index number

groceries_list.insert(2, 'Watermelon')
print(groceries_list)

# count() gives us number of the element in the list

nums5 = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1]

print(nums5.count(1))

print('-------------------------------------------------')

# List COMPREHENSION Practices

nums6 = []

for x in range(1, 51):
    nums6.append(x)
print(nums6)

print('-------------------------------------------------')

# LIST COMPREHENSION

# new_list = [ var_name for var_name in iterable if condition ]

# divisible_by_5 = []
#
# for y in nums6:
#     if y % 5 == 0:
#         divisible_by_5.append(y)
# print(divisible_by_5)

# above is the solution with loop. but we can do with list comprehension by using only one row.

divisible_by_5 = tuple([x for x in nums6 if x % 5 == 0])

print(divisible_by_5)

# TUPLE is not supported by COMPREHENSION

print('-------------------------------------------------')

even_nums = [x for x in nums6 if x % 2 == 0]
odd_numbers = [x for x in nums6 if x % 2 != 0]
print(odd_numbers)
print(even_nums)

print('-------------------------------------------------')

# to remove string elements by using comprehension

names2 = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names2 = [x for x in names2 if x.lower() != 'java']

print(names2)