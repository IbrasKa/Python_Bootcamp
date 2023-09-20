name = input('Enter your name:\n')
age = int(input('Enter your age:\n'))
gender = input('Enter your gender:\n')
company = input('Enter your company name:\n')
job_title = input('Enter your job title:\n')
salary = float(input('Enter your salary:\n'))

print(f"{name} is {age} years old, gender is {gender}\n"
      f"{name} works at {company} as a {job_title}\n"
      f"{name} makes £ {salary} pear year")