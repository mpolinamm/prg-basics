monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

total_expences_food = 0
total_expences_transport = 0
total_expences_utilities = 0
weekly_totals = []
monthly_total = 0
for week in monthly_expenses:
    total_expences_food += week[0]
    total_expences_transport += week[1]
    total_expences_utilities += week[2]

    weekly_total = sum(week)
    weekly_totals.append(weekly_total)

    monthly_total += weekly_total

print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_expences_food)
print('Transport:',total_expences_transport)
print('Utilities:',total_expences_utilities)
print('Week 1:',weekly_totals[0])
print('Week 2:',weekly_totals[1])
print('Week 3:',weekly_totals[2])
print('Week 4:',weekly_totals[3])
print('---------------')
print('TOTAL:',monthly_total)