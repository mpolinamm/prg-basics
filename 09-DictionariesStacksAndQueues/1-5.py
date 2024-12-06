countries = [
{"name":"Poland", "population":38000000},
{"name":"Ukraine", "population":37000000},
{"name":"Germany", "population":80000000},
{"name":"France", "population":40000000},
{"name":"Australia", "population":26000000}
]
print(f"{'COUNTRY':<10} {'POPULATION':<10}")

for entry in countries:
    print(f"{entry['name']:<10} {entry['population']:<10}")