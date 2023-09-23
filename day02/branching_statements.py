for i in range(1, 6):
    if i == 3:
        break   # EXITS THE LOOP
    print (i)

print('-------------------------------------------------')

for i in range (1, 6):
    if i == 3 or i == 4:
        continue    # SKIPS TO THE NEXT ITERATION
    print(i)

print('-------------------------------------------------')

for i in range (1, 6):
    if i == 3 or i == 4:
        pass    # NOTHING HAPPENS. RESULTS IS NO OPERATION. IT IS USED A PLACEHOLDER
    print(i)


def function ():
    pass

if True:
    pass

class Class:

    def method(self):
        pass

    pass