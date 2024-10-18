account_balance = 500
total_payment = float(input("The total value of purchases: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')