# import utility
from utility import sum, calculate # similar to static import Java

result = sum(10, 20, 30)
print(result)

result2 = calculate(66, 88, '*')
print(result2)

import utility
utility.concat("Java", "Python")
utility.sum(10,20)
utility.calculate(10, 20, '*')

print('-------------------------------------------------')
# Alias = Temporary Name

import  utility as uti
uti.sum(10,20)
uti.concat('A', 2, 3)
uti,calculate(20,30,'/')

print('-------------------------------------------------')

from utility import sum as s
print(s(10,20))