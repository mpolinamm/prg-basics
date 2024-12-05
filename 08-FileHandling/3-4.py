import re  

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

pattern = r'€\d+'

amounts = re.findall(pattern, email)

total = 0
for amount in amounts:
    total += float(amount[1:]) 

# Print the result
print(f"Total money spent: €{total:.2f}")