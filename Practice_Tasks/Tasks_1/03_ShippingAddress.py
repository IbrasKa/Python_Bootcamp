
"""
Create a python file named ShippingAddress. Declare the following variables:
                    name
                    building_number
                    street_name
                    city
                    state
                    zip_code

    Use concatenation to print the full shipping address

        Ex:
            Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""

name = 'Gedon LLC'
building_number = 12
street_name = 'Melashvili Street'
city = 'Warsaw'
state = 'Poland'
zip_code = '00-021'

print(f"Your shipping address is:\n\t\t{name}\n\t\t{building_number}"
      f"\n\t\t{street_name}\n\t\t{city}\n\t\t{state}\n\t\t{zip_code}")