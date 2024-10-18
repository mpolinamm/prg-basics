basic_salary = 5000
total_salary = 0
is_bonus = False
bonus = 0.3 

if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')