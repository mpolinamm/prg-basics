with open('countries.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
        country, capital, population = line.strip().split(', ')
        print(f"{index}. {country}, {capital}, {population}")