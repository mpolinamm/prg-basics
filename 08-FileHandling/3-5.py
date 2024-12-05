import re

username = input("Create username: ")
password = input("Create password: ")

username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

if username_match and password_match:
   print("You succesfully created username and password")
else:
   print("Username and/or password don't match a pattern")