# Lists
letters = ["a", "b", "c", "d", "e"] # list syntax
matrix = [[0, 1], [1, 2]] # list inside list (nested list)
zeros = [0] * 5 
combined = zeros + letters # concatination of list
print(combined)

# iterable list function
numbers = list(range(20))
print("\n\n")
print(numbers)

chars = list("HELLO WORLD")
print("\n\n")
print(chars)
print(len(chars))  # length of the list

# indexing
print("\n\n")
print(letters[0])

letters[0] = "A"

print(letters)

print(letters[0:3])

print(letters[::2])  # skipping the index as given in the value

# unpacking the list
print("\n\n")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first = num[0]
# second = num[1]
first, second, third, *others, last = num # unpacking the list
print(first)
print(second)
print(third)
print(others)
print(last)

# loops in lists
items = ["a", "b", "c"]
print("\n\n")
for item in items:
    print(item)
for item in enumerate(items): # indexing each item in the list
    print(item)

