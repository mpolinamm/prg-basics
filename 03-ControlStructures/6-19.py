print('SURVEY')
question1 = input('Are you interested in computer science? (y/n): ') == 'y'
question2 = input('Do you like playing computer games? (y/n): ') == 'y'
question3 = input('Do you have an Instagram account? (y/n): ') == 'y'
if question1:
    result1 = 'Yes'
else:
    result1 = 'No'
if question2:
    result2 = 'Yes'
else:
    result2 = 'No'
if question3:
    result3 = 'Yes'
else:
    result3 = 'No'

print('SURVEY RESULTS')
print(f'Interested in computer science:{result1}')
print(f'Playing computer games:{result2}')
print(f'Has an Instagram account:{result3}')