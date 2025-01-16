sentence = 'I completely agree with you'

words = sentence.split()

letter_counts = list(map(lambda word: len(word), words))

print(f"Text: {sentence}")
print(f"Number of letters in words: {letter_counts}")
