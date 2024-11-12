jacket_time = 40
underwear_time = 70
shoes_time = 20
rinse_time = 15
spin_time = 9
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').strip().lower()
extra_rinse = input('Extra rinse? (y/n): ').strip().lower()
extra_spin = input('Extra spin? (y/n): ').strip().lower()
if program == 'j':
    total_washing_time += jacket_time
    washing_product = "jacket"
elif program == 'u':
    total_washing_time += underwear_time
    washing_product = "underwear"
elif program == 's':
    total_washing_time += shoes_time
    washing_product = "shoes"
else:
    print("Invalid program selection.")
    exit()
if extra_rinse == 'y':
    total_washing_time += rinse_time
if extra_spin == 'y':
    total_washing_time += spin_time
print(f"washing_product = \"{washing_product}\"")
print(f"rinse = {extra_rinse == 'y'}")
print(f"spin = {extra_spin == 'y'}")
print(f"Total washing time: {total_washing_time} minutes")
