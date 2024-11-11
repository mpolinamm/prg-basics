name = input('Enter a female name: ')
last_letter = name[-1]
if last_letter == 'a':
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a typical Polish female name')