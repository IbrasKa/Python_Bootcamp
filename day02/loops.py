

s = 'Python Programming'

for each in s:
    print(each)


print('-------------------------------------------------')

# Let's print the index number

for i in range (0, len(s)):
    print(s[i])


print('-------------------------------------------------')

# Can I print the reversed index number

for i in range (-len(s),0):
    print(s[i])

print('-------------------------------------------------')

# Can I print the reversed string

for i in reversed(range(0, len(s))):
    print(s[i])

print('-------------------------------------------------')

for x in s[::-1]:       # String'i reverse etmenin diger yolu. Her ikisini de kullanabilirsiniz.
    print(x,end="")     # end=""--> Ayni satirda print eder.


print('\n-------------------------------------------------')

# Ayni satirda print etmek icin kullanabilecek baska opsiyon :

result = ''
for x in s[::-1]:
    result += x
print(result)

print('-------------------------------------------------')

# Write a programme to ask the user to input a positive number and display the number

num = int(input('Enter a positive number:\n'))

while num <= 0:
    num = int(input('Enter a positive number:\n'))

print(f"You entered {num}")

print('-------------------------------------------------')

# I want to ask the user to say yes or no
answer = input('Enter yer os no:\n')
count = 0
while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yer os no:\n')
    count += 1
print (f'{count} kere girdin')
print(f"You have entered {answer}")