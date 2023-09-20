name = input("1.1.1 \"Enter your name:\n")
hourly_rate = float(input("1.1.2 \"Enter your hourly rate:\n"))
weekly_hours = float(input("1.1.2 \"How many hours you work in a week?\n"))

salary = (hourly_rate * weekly_hours * 52)

print(f"Hello {name}, your salary is £ {salary}")
