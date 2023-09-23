
"""
create a python file named phone_number and declare the following variables:
            countryCode, areaCode, localNumber

            use string concatenation to display the phone number
            ex:
                if  country_code = 1
                    area_code = 703
                    localNumber = 4512625

                output:
                    Your phone number is +1(703)-4512625
"""

country_code = 44
area_code = 19
local_number = 23956529

if country_code == 44 and area_code == 19 and local_number == 23956529:
   print(f"Your phone number is +{country_code}({area_code})-{local_number}")
else:
    print('Wrong country_code or area_code or local_number')