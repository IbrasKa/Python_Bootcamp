"""
1.1 Write a program that can move all the zeros to the last indexes of ArrayList
# 	            Ex:
# 	                list: [1,0,2,0,3,0,4,0]
#
# 	            output:
# 	                [1, 2, 3, 4, 0, 0, 0, 0]
"""

num_list = [1, 0, 2, 0, 3, 0, 4, 0]


def move_zero_to_end(list1: list):
    move_zero_list = []

    for x in list1:
        if x != 0:
            move_zero_list.append(x)

    for y in list1:
        if y == 0:
            move_zero_list.append(y)

    print(move_zero_list)


move_zero_to_end(num_list)

print('-------------------------------------------------')

"""
1.2 write a program that can multiply each odd number by 2
# 		            ex:
# 		            	list = [1,2,3,4,5];
#
# 		                output: [2,2,6,4,10]
"""

num_list2 = [1, 2, 3, 4, 5]


def multiply_odd_list(list2: list):
    multiply_list = []

    for x in list2:

        if x % 2 != 0:
            multiply_list.append(x * 2)

        elif x % 2 == 0:
            multiply_list.append(x)

    print(multiply_list)


multiply_odd_list(num_list2)

print('-------------------------------------------------')

"""
1.3 Write a program that can remove all the names "Ahmed" from a list of strings
# 				Ex:
# 	                list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]
#
# 	            output:
# 	            	["John", "Daniel", "James", "Muhammed"]
"""

list3 = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

list3.remove('Ahmed')

print(list3)

print('-------------------------------------------------')

"""
1.4 Write a program that can display the palindrome strings from a list of String
# 				Ex:
# 					words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']
#
# 					output:
# 						Anna
# 						Level
"""
words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']


def find_palindrome(list4: list):
    for x in list4:

        if x.lower() == x.lower()[::-1]:
            print(x)


find_palindrome(words)

print('-------------------------------------------------')

"""
1.5 Write a program that can display the common elements of two lists:
# 				Ex:
# 					list1 = [1,2,3,4,5]
# 					list2 = [4,5,6,7,8]
#
# 					Output:
# 						4
# 						5
"""
list5 = [1, 2, 3, 4, 5]
list6 = [4, 5, 6, 7, 8]


def common_elements(list1: list, list2: list):
    for x in list1:
        for y in list2:
            if x == y:
                print(x)


common_elements(list5, list6)

print('-------------------------------------------------')

"""
1.6 Write a program that can remove the duplicated elements from a list
# 				Ex:
# 					elements = [1,2,3,4,5,1,2,3,4,5]
#
# 					Output:
# 						[1, 2, 3, 4, 5]
#
# 					Notes: Do Not use Set
"""

elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def remove_elements(list1: list):
    final_list = []

    for x in list1:

        if x not in final_list:
            final_list.append(x)
    print(final_list)


remove_elements(elements)

print('-------------------------------------------------')

"""
1.7 Write a program that can remove string elements from a list if the first and last characters of the string are
#           same ex: list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}
#
# 				output:
# 					["Lan", "Ebrahim", "Farida"]
"""
elements = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}


def remove_string_elements(list1):
    final_list = []

    for x in list1:
        if x.lower()[0] != x.lower()[len(x) - 1]:
            final_list.append(x)
    print(final_list)


remove_string_elements(elements)

print('-------------------------------------------------')

"""
1.8  Write a program that can display the unique elements of an arrayList:
# 					ex:
# 						list = [1, 1, 2, 3, 3, 4, 5, 5]
#
# 					output:
# 						[2, 4]
"""

# elements = [1, 1, 2, 3, 3, 4, 5, 5]
#
#
# def unique_elements(list1: list):
#     pass
#
#
# unique_elements(elements)
