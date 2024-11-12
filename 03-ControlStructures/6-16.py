washing_product = input('Enter the washing product (jacket/underwear/shoes): ')
if washing_product == 'jacket':
    washing_time = 40
elif washing_product == 'underwear':
    washing_time = 70
elif washing_product == 'shoes':
    washing_time = 20
else:
    print("You can't use this washing machine for this product!")
print("Would you like to rinse or/and spin your product? (Enter True if yes, False otherwise)")
rinse_input = input("Rinse (True/False): ").strip().lower()
spin_input = input("Spin (True/False): ").strip().lower()
rinse = rinse_input == 'true'
spin = spin_input == 'true'
rinse_time = 15
spin_time = 9
if (rinse and spin):
    total_time = washing_time + rinse_time + spin_time
elif rinse:
    total_time = washing_time + rinse_time
elif spin:
    total_time = washing_time + spin_time
else:
    total_time = washing_time
print(f'Total washing time: {total_time} minutes')