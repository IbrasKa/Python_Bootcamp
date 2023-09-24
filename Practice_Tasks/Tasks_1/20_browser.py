
"""
Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""
browser_name = 'sAfArI'

if type(browser_name) == str:
    if browser_name.lower() == 'chrome':
        print('Chrome browser selected')
    elif browser_name.lower() == 'firefox':
        print('Firefox browser selected')
    elif browser_name.lower() == 'opera':
        print('Opera browser selected')
    elif browser_name.lower() == 'safari':
        print('Safari browser selected')
    elif browser_name.lower() == 'edge':
        print('Edge browser selected')
    else:
        print('Invalid browser name')
else:
    print('Invalid browser name')