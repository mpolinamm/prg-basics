test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)

correct_answers = 0
for answer in test_results:
   if answer == True:
     correct_answers += 1 

incorrect_answers = 0
for answer in test_results:
   if answer == False:
     incorrect_answers += 1 

percentage_correct = correct_answers * 100 / question_number

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f"Percentage of correct answers: {percentage_correct:.2f} %") 