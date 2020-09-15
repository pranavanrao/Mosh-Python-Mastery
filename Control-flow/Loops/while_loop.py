num = 100
while num > 0:
    print(num)
    num = num // 2

# another example
command = ""
while command.lower() != "quit":
    command = input('Input the command : ')
    print('ECHO', command)