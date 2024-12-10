names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

print("Names:", " ".join(names))

longest_name = names[0]
for name in names:
    if len(name) > len(longest_name):
        longest_name = name
print("Longest name:", longest_name)