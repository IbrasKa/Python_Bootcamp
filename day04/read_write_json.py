import json

path = 'files/Test.json'

jason_file = open(path, 'r')

# print(type(jason_file.read()))  # type of file is string. to convert the dictionary we need to use json module (json.load)

dictionary = json.load(jason_file)  # converting json object to dictionary

print(dictionary)
print(type(dictionary))

for x in dict(dictionary).keys():
    print(x)

jason_file.close()

print('--------- Writing json file -----------------')

dictionary['name'] = 'Aaron King'
dictionary['age'] = 45

print(dictionary)

jason_file2 = open('files/Test2.json','w')

json_object2 = json.dumps(dictionary, indent=2)   # dictionary to jason object

jason_file2.write(json_object2)

jason_file2.close()

print('--------- Writing json file -----------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

jason_file3 = open('files/Test3.json', 'w')

json_object3 = json.dumps(students, indent=3)     # # converting dictionary to json object

jason_file3.write(json_object3)


"""
Web automation icin kullanilan package
    BeautifulSoup4
    request
    pytest
    robot

Web development icin kullanilan package
    Django
    FastAPI
    flask
"""