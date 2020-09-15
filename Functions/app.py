# using arguments
def greet(first_name, last_name, designation):
    print(f"Hi {first_name} {last_name}")
    print(designation)

greet("Pranav", "Rao", "Full Stack Developer")

# return functions
def greeting(name):
    return f"Hi {name}!!!"

message = greeting("Pranav")
print("\n\n")
print(message)

# readable arguments
def increment(num1, num2):
    return num1 + num2

print("\n\n")
print(f"Increment is {increment(num1=2, num2=3)}")

# default arguments
def increment1(x, y=1):
    return x + y

print("\n\n")
print(f"First Increment is {increment1(2)}")
print(f"Secong increment is {increment1(5)}")

# xrags
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("\n\n")
print(multiply(1, 2, 3, 4))

# xxrags
def save_users(**user):
    print(user)

print("\n\n")
save_users(id=1, name="Pranav N Rao")