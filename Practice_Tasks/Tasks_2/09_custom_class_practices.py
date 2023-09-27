"""
9. Create a python file named custom_class_practices:
        9.1 Create a custom class named Pizza:
        Attributes:
            size, numberOfCheeseTopping, numberOfPepperoniTopping

            Add a constructor that can set all the fields
        Actions:
            calcCost(): returns the totalCost of the pizza
            __str__():returns a String containing the pizza size, quantity of each topping, and the pizza cost
            as calculated by calcCost()

        Pizza cost is determined by:
                        S: $10 + $2 per topping
                        M: $12 + $2 per topping
                        L: $14 + $2 per topping

"""
import numbers
from math import pi


class Pizza:

    def __init__(self, size: str = 'Unknown', numberOfCheeseTopping: int = 0, numberOfPepperoniTopping: int = 0):
        self.size = size
        self.numberOfCheeseTopping = numberOfCheeseTopping
        self.numberOfPepperoniTopping = numberOfPepperoniTopping

    def calCost(self):
        if self.size.lower() == 's':
            print(
                f"The Total Cost of Pizza: £{10 + self.numberOfCheeseTopping * 2 + self.numberOfPepperoniTopping * 2}")
        elif self.size.lower() == 'm':
            print(
                f"The Total Cost of Pizza: £{12 + self.numberOfCheeseTopping * 2 + self.numberOfPepperoniTopping * 2}")
        elif self.size.lower() == 'l':
            print(
                f"The Total Cost of Pizza: £{12 + self.numberOfCheeseTopping * 2 + self.numberOfPepperoniTopping * 2}")
        else:
            print('Incorrect Pizza Type. Please choose again')

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}"


pizza = Pizza('s', 3, 6)

print(pizza)
pizza.calCost()

"""
9.2 Create a class named Circle:
                Attributes:
                    instance: radius
                    static: pi

                Add a constructor that can set All the fields (instances)
                    
                Actions:
                    calcArea(): returns the area of Circle

                    calcPerimeter(): returns the perimeter of Circle

                    __str__(): displays the radius, diameter, pi, area and perimeter of the circle when the 
                    object of circle is passed in the print statemen
"""


class Circle:
    pi = pi

    def __init__(self, radius: numbers):
        self.radius = radius
        self.pi = pi

    def calcArea(self):
        area = round(pi * self.radius * self.radius, 2)
        return area

    def calcPerimeter(self):
        perimeter = round(2 * pi * self.radius, 2)
        return perimeter

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}"


circle = Circle(5)
print(f"The area of the circle : {circle.calcArea()}, perimeter of the circle : {circle.calcPerimeter()}")
print(circle)