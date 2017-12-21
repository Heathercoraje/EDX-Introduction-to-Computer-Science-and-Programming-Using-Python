# Paste your code into this box
# no function wrapper
# first, create variables to reuse

monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
newBalance = balance # initial balance

while (newBalance > 0):
     # if updated balance is bigger than 0, reset the balance and add $10 to monthlypayment and repeat
    monthlyPayment += 10
    newBalance = balance
    month = 1

    while (month <= 12) and (newBalance > 0):
        newBalance -= monthlyPayment
        interest = newBalance * monthlyInterestRate
        newBalance += interest
        month += 1
    newBalance = round(newBalance, 2)
print(monthlyPayment) 
