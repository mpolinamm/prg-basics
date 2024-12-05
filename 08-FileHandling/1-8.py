with open('pets.txt', 'r') as file:
    lines = file.readlines()
total_words = 0
print("Text from 'pets.txt':")
for line in lines:
    print(line.strip()) 
    word_count = len(line.split())
    total_words += word_count
print("\nTotal number of words in the text:", total_words)
