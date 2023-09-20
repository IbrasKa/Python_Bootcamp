num = int (input('Enter a level number (1~18):\n'))

if 18>= num >= 1 :
    if num <=5:
        print('Your school type is Elementary School')
    elif num <=8:
        print('Your school type is Middle School')
    elif num <= 12:
        print('Your school type is High School')
    elif num <= 16:
        print('Your school type is College')
    else:
        print('Your school type is Grad School')
else :
    print('Invalid level number. Please try again')
