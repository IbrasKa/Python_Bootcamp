"""
# 3. Create a python file named inheritance_practice:
# 		Create an abstract class named Animal:
# 	        Variables:
# 	            name, breed(final), gender(final),  age, size, color(final)
# 	        Encapsulate all the fields
# 	        Add a constructor that can set all the fields
# 	        Methods:
# 	            eat() ==> different animals eat different foods
# 	            drink() ==> all the animals drink water
# 	            toString() ==> to display the full info of the animal
# 		    Create the following subclasses of Animal:
# 		            Dog
# 		                eat(): Dog Food
# 		            Cat
# 		                eat(): Cat Food
# 		            Parrot
# 		                eat():
# 		            Eagle
"""


class Animal:

    def __init__(self, name: str, food: str, BREED: str, GENDER: str, COLOUR: str, age: int = 0, size: str = ''):
        self.name = name
        self.BREED = BREED
        self.GENDER = GENDER
        self.age = age
        self.size = size
        self.COLOUR = COLOUR
        self.food = food

    def eat(self):
        return f"{self.name} is eating {self.food}"

    def drinks(self):
        return f"drinks water"

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}, {self.eat()} and {self.drinks()}"


class Dog(Animal):

    def __init__(self, name: str, food: str, BREED='Pit Bull', GENDER= 'Male', COLOUR='White and Black', age: int = 0, size: str = ''):
        super().__init__(name, food, BREED, GENDER, COLOUR, age, size)

        self.BREED = 'Pit Bull'
        self.GENDER = 'Male'
        self.COLOUR = 'White and Black'

    def eat(self):
        return f" {self.name} is eating {self.food}"


class Cat(Animal):

    def __init__(self, name: str, food: str, BREED='Turkish Van', GENDER='Female', COLOUR='White', age: int = 0,
                 size: str = ''):
        super().__init__(name, food, BREED, GENDER, COLOUR, age, size)

        self.BREED = 'Turkish Van'
        self.GENDER = 'Female'
        self.COLOUR = 'White'

    def eat(self):
        return f" {self.name} is eating {self.food}"


class Eagle(Animal):

    def __init__(self, name: str, food: str, BREED='Golden Eagle', GENDER='Male', COLOUR='Golden-brown', age: int = 0,
                 size: str = ''):
        super().__init__(name, food, BREED, GENDER, COLOUR, age, size)

        self.BREED = 'Golden Eagle'
        self.GENDER = 'Male'
        self.COLOUR = 'Golden-brown'

    def eat(self):
        return f" {self.name} is eating {self.food}"


dog1 = Dog('Sepet', 'Beef', 'Karabas', 'Female')
print(dog1)

cat1 = Cat('Premses', 'Cheese')
print(cat1)
#
eagle1 = Eagle('Tirsik', 'Fish')
print(eagle1)
