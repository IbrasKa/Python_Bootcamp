"""
# 2. Create a python file named encapsulation_practice:
# 		create a class called Item
# 		    private variables:
# 		        name, unit_price, quantity
#
# 		    Encapsulate all the fields:
# 		        Conditions:
# 		            name can not be empty
# 		            unit price can not be negative
# 		            quantity can not be negative
#
# 		        If invalid data are given to set the firled, then make sure to throw an error duribg the runtime.
# 		        	(hint: you can use 'raise RuntimeError('Exception message')')
#
#
# 		    Add a constructor that allows user to set all the fields when the object is created.
# 		            (If the arguments not valid it should not be set to the instances)
#
# 		    Methods:
# 		        calcCost(): returns the total cost
# 		        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()
"""
import numbers


class Item:
    def __init__(self, name: str, unit_price: numbers, quantity: int):
        self.__name = name
        self.__unit_price = unit_price
        self.__quantity = quantity
        self.item_name = name
        self.item_quantity = quantity
        self.item_unit_price = unit_price

    @property
    def item_name(self):
        return self.__name

    @property
    def item_unit_price(self):
        return self.__unit_price

    @property
    def item_quantity(self):
        return self.__quantity

    @item_name.setter
    def item_name(self, name):

        if type(name) != str:
            raise RuntimeError(f"Person name must be string")

        if name == '':
            raise RuntimeError(f"Person name can not be empty")

        self.__name = name

    @item_unit_price.setter
    def item_unit_price(self, unit_price):

        if unit_price <= 0:
            raise RuntimeError(f"unit price ({unit_price}) must be bigger than zero")

        self.__unit_price = unit_price

    @item_quantity.setter
    def item_quantity(self, quantity):

        if type(quantity) != int:
            raise RuntimeError(f"type of quantity ({type(quantity)}) must be an integer")

        if quantity <= 0:
            raise RuntimeError(f"quantity ({quantity}) must be bigger than zero")

    def __str__(self):

        return f"{type(self).__name__}{self.__dict__}, Total cost: {self.calcCost()}"

    def calcCost(self):

        return f"Total price of {self.__quantity} {self.__name}s are £{self.__quantity * self.__unit_price}"


item1 = Item('elma', 3.98, 28)
print(item1)
