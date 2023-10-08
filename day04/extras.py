from functools import reduce

print('-------------closure--------------------------')


# closure means NESTED FUNCTION

def display_message():
    def method():
        print('Hello World')
        print('I love Python')

    method()
    method()
    method()
    method()


display_message()


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s.lower()

    for s in strings:
        if is_palindrome(s):
            print(s)


print('-------------map (Lambda)(list)--------------------------')

nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map(lambda x: x * 10, nums))

print(nums)

names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

names = list(map(lambda s: str(s).upper(), names))

print(names)

print('-------------map (Lambda)(dictionary)--------------------------')

dictionary = {'x': 100, 'y': 200, 'z': 300}

dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items()))

print(dictionary)

print('-------------filter(Lambda)--------------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# nums = [ x for x in nums if x % 5 ==0]

nums = list(filter(lambda x: x % 5 == 0, nums))

print(nums)

names = ['Java', 'JAVA', 'java', 'ruby', 'swift', 'CyDeO', 'javaSCRipt']

# names = [a for a in names if not a.lower().startswith('j')]

# making it with list comprehension
# 1. Declare a variable
# 2. Use this variable in the list to get every single element
# 3. Write the condition
names1 = [a for a in names if not a.lower().startswith('j')]
print(names1)

# making it with FILTER method
names = list(filter(lambda x: not str(x).lower().startswith('j'), names))

print(names)

print('-------------reduce(Lambda)--------------------------')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# If I want to sum all the integers in the list1
print(reduce(lambda x, y: x + y, list1))

list2 = ['Java', 'Python', 'C#', 'Ruby']
# to convert list2 object to one string object we can use reduce method
print(reduce(lambda x, y: f'{x} {y}', list2))
print(type(reduce(lambda x, y: f'{x} {y}', list2)))  # type is strings
