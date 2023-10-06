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

from typing import final


class Animal:

    def __init__(self, name: str, food: str, breed: str, gender: str, colour: str, age: int = 0, size: str = ''):
        self.name = name
        self.__BREED = breed
        self.__GENDER = gender
        self.__COLOUR = colour
        self.age = age
        self.size = size
        self.food = food

    @property
    def animal_breed(self):
        return self.__BREED

    @animal_breed.setter
    def animal_breed(self, breed):
        raise RuntimeError(f'breed is constant, can not be changed')

    @property
    def animal_gender(self):
        return self.__GENDER

    @animal_gender.setter
    def animal_gender(self, gender):
        raise RuntimeError(f'gender is constant, can not be changed')

    @property
    def animal_colour(self):
        return self.__COLOUR

    @animal_colour.setter
    def animal_colour(self, colour):
        raise RuntimeError(f'gender is constant, can not be changed')

    @final
    def eat(self):
        return f"{self.name} is eating {self.food}"

    @final
    def drinks(self):
        return f"{self.name} is drinking water"

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}, {self.eat()} and {self.drinks()}"


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Eagle(Animal):
    pass


dog1 = Animal('Sepet', 'Beef', 'Karabas', 'Male', 'Black', 9, 'Medium')
print(dog1)
dog1.animal_breed = 'Pitbull'
print(dog1)
