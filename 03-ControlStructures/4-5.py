plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_encoded = ord(char)
    char_encoded = char_encoded + 1
    encrypted_text = encrypted_text + chr(char_encoded)
print(plain_text)
print(encrypted_text)