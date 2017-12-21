monthlyInterestRate = annualInterestRate/12.0
newBalance = balance
lowerBound = balance/12
upperBound = (balance*((1+monthlyInterestRate)**12))/12

while (newBalance > 0):
    newBalance = balance
    month = 1
    target = round((lowerBound + upperBound)/2,2) # by cent

    while (month <= 12):
        newBalance -= target
        interest = monthlyInterestRate * newBalance
        newBalance += interest
        month += 1
    newBalance = round(newBalance, 2)

    if (int(newBalance) > 0):
        lowerBound = target
    elif (int(newBalance) < 0 ):
        upperBound = target
    else:
        break
        print('Lowest Payment: ', target)
print('Lowest Payment: ', target)
