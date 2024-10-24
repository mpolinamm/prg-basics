plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha(): 
        char_encoded = ord(char)
        char_encoded = char_encoded + 1
        encrypted_text += chr(char_encoded)
    else:
        encrypted_text += char  
print(plain_text)
print(encrypted_text)