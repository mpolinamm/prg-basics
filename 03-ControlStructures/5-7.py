import time
number_words = {5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}
countdown_start = int(input("Enter a number to start the countdown: "))
for i in range(countdown_start, 0, -1):
    if i in number_words:  
        print(number_words[i])
    else:
        print(i)
    
    time.sleep(1) 
print("Time's up!")
