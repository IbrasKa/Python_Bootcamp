"""
5. Create a python file named characters, write a program that can retrieve the digits, letters and special characters from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!

"""


def retrieveCharacter(expression: str = ''):
    letter = ''
    digits = ''
    specialChar = ''
    space = 1
    for i in range(0, len(expression)):
        if expression[i].isalpha():
            letter += expression[i]
        elif expression[i].isdigit():
            digits += expression[i]
        elif expression[i].isspace():
            space += 1
        elif not (expression.isspace() and expression.isalpha() and expression.isdigit()):
            specialChar += expression[i]

    print(f'letters : {letter}\ndigits : {digits}\nspecial chars : {specialChar}\nspace : {space} times')


retrieveCharacter('mn@#123Ab! tyopy msfp-43-v dnkksa]-q=3 d]ow-r   p[f[]da ')
