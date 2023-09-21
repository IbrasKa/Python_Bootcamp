name = 'Python'

print(len(name))
print(name[0])
print(len(name)-2)

print(name[-1])
print(name[-2])
print('-------------------------------------------------')

#Slicing
s = 'Java Programming Language'

s2 = s[5:16]

print(s2)

s3 = s[:4]
print(s3)
print('-------------------------------------------------')

#Reverse String
s4 = s[::-1]
print(s4)
print('-------------------------------------------------')

#Reversed order
s = 'Python Programming'
#to get the reversed object, there is reversed method
# s5 = str(reversed(s))
#
# print(type(s5))
# reversed(s5)
# print(s5)
print(s[::-1])
print('-------------------------------------------------')

s7 = 'CYDEO SCHOOL'
#reversed(s7)

print('-------------------------------------------------')
#print(help(str))

print('-------------------------------------------------')

s = 'python programming language'

#to capitalise the first letter
s = s.title()
print(s)
print('-------------------------------------------------')

#to delete white spaces from left&right side
s = "                 Python                       "
#delete left space
s = s.lstrip()
print(s)

#delete right space
s = s.rstrip()
print(s)

#to remove all spaces, use stripe() method
s = s.strip()
print(s)
print('-------------------------------------------------')

s = 'JAVA ABA'
print(s.index('A'))
print(s.rindex('A'))

s = 'Java Java'

s = s.replace('Java', 'Python',1)
print(s)

#to change the second (bosluklara dikkat!)
s = 'C# C# Python'

s = s.replace(' C#', ' Java')
print(s)

#count() method is used for count of frequency

s = 'aaaaaaaawrearwwwwwwaaaaaaaaddddddddxxxxxxxxssssaaaaaaaaaghhytsssaaassssa'
count_a = s.count('a')
print(count_a)

#to get to ignore case sensitivity
s = 'Java jAVA java JAVA Python Python'
count_java = s.lower().count('java')
print(count_java)

#As there is no equalignorecase method in Python,  we use equal (==) operator
s1 = 'java'
s2 = 'JAVA'
print(s1.lower()==s2.lower())

s = 'Java'

print(s[0].islower())
