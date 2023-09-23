
"""
Create a python file named shipping_address
            Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""


name = input('Enter your full name:\n')
building_number = input ('Enter your building number:\n')
street = input('Enter your street name:\n')
city = input('Enter your city name:\n')
state = input('Enter your state name:\n')
zip_code = input('Enter your zip code:\n')

print(f"Your shipping address is :\n\t\t{name}\n\t\t{building_number} {street}"
      f"\n\t\t{city}, {state} {zip_code}")
