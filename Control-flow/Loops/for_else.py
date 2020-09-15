# For..else
success = False #put true boolean to check another posibility
for number in range(3):
    print('Attempt', number + 1)
    if success:
        print('SUCCESSFULL!!!')
        break
else:
    print('Attempted 3 times and failed!!!')