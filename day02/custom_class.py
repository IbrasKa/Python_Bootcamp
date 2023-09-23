import numbers


class Employee:

    is_human = True # similar to static variable in Java
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0): # Argument values is default values
        self.name = name        # These are INSTANCE Variables.
        self.job_title = job_title
        self.salary = salary

    def work (self):
        print(f"{self.name} works as a {self.job_title} at Sky")

    def __str__(self):  # declaring toString Method in Python. 
        return f"{type(self).__name__}{self.__dict__}"


# to create the object from above class

employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

# ARGUMENT'lerde DEFAULT value vermemizin sebebi istedigimiz kadar argument'i pass etmek icin.

employee2 = Employee('Ali') # Burada 3 argument'i pass etmek yerine 1'sini ettik
print(employee2.name)



employee3 = Employee('Breanna', 'SDET') # Burada 3 argument'i pass etmek yerine 2'sini ettik
print(employee3.name)
print(employee3.job_title)


employee4 = Employee('Yulia', 'Python Developer', 150_000) # Burada 3 argument'i pass ettik
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

# print(Employee.name) # As this is static variable we can't access it. There is no static variables in Python.
# You can create static variable outside of the constructor and inside the class.
# What if we do to access to static variables?
print(employee1.is_human)
print(employee4.planet)

print(employee1.job_title)

employee1.work()
employee2.work()
employee3.work()
employee4.work()

print(employee1)
print(employee2)
print(employee3)
print(employee4)


