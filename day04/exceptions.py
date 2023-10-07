try:
    num = 10 / 0
    print(num)

except:  # gets executed when try block gives an ERROR
    print('Something went wrong')

else:
    print('Nothing went wrong')  # gets executed when try blocks gives NO ERROR

finally:  # always gets executed.
    print('finally block')

print('Test completed')

print('-------------------------------------------------')

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2])
except:
    print('The index number is too large')
else:
    print('The index number is valid')

print('-------------------------------------------------')

# If you want to give multiple EXCEPT block:

try:
    raise FileNotFoundError ('No such a file')
except SyntaxError:
    print('It is syntax error')
except OSError:
    print('It is an OS error')
except ArithmeticError:
    print('It is an arithmetic error')
# else:
#     print('No error has occured')   # Butum olasiliklari except olarak verdigimiz icin bu UNREACHABLE

finally:
    print('finally block')

print('-------------------------------------------------')

