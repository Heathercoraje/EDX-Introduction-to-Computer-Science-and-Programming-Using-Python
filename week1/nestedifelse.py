x = (input('enter an int: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 but not by 3')
elif x%3 == 0:
    print('Divisible by 3 but not by 2')
else:
    print('Not divisible either 3 or 2')
print('I am done')
