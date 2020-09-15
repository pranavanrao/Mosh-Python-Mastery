# Conditional statements

# ternary operators
temperature = 15
if temperature > 30:
    print("It's warm, drink water")
elif temperature > 20:
    print("It's cold")
else:
    print("It's freezing")
print("Anyways, drink water!")

# alternative to ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not elegible"
print(message)

# logical operators
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not eligible')

# Changing comparison operators
if 18 <= age < 65:
    print('Eligible between 18 to 65')
