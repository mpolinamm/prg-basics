original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open('healthy_lifestyle.txt', 'r') as file:
   content = file.read()

text = content

with open('copy_healthy_lifestyle.txt', 'w') as file:
   file.write(text)

print(f"The content has been coppied to {target_file}. Check the file to verify the contents.")