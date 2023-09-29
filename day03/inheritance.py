class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}"


class Employee(Person):

    def __init__(self, name: str, age: int, job_title: str, company_name: str = '', salary: int = 0):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")


class Developer(Employee):

    # if we don't need additional variable for this subclass we can use pass. Block can not be empty. we are using pass

    # def __init__(self, name: str, age: int, job_title: str = 'Software Developer', company_name: str = 'Unknown'):
    #     super().__init__(name, age, job_title, company_name)

    # """
    #     if you don't need any additional variable then you don't need to create constructor on child class.
    #     Yukaridaki ornekte butun variable'lar Employee class'ta declare edilmis. Dolayisiyla burada tekra constructor
    #     kullanmaya gerek yok.
    # """

    def work(self):
        print(f"{self.job_title} {self.name} is coding")


class Teacher(Employee):

    # If I don't need to create any additional variable, then I don't need to call employee constructor we must pass
    # name, age and job title argument which is coming from employee class. what if I pass only 2 arguments? Then I
    # need to create constructor manually.

    def __init__(self, name: str, age: int, job_title: str = '', company_name: str = '', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)

        # Abow constructor, we must pass only 2 argument as the rest has default values


    def work(self):
        print(f"{self.name} is teaching")


# Let's create objects from classes

employee1 = Employee('Hazel', 27, 'QA', 'Apple Inc')
developer1 = Developer('Daniel', 35, 'Python Developer', 'Google Inc', 100_000)
teacher1 = Teacher('Fiona', 33)

print(employee1)
print(developer1)
print(teacher1)

employee1.work()
developer1.work()
teacher1.work()
