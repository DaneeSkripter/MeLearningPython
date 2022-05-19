import os
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file == "encryptor.py" or file == "decryptor.py" or file == "yek.key":
        continue
    if os.path.isfile(file):
        files.append(file)
    

with open("yek.key", "rb") as thekey:
    key = thekey.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
    old_name = file.encode('utf-8') 
    name_decrypted = Fernet(key).decrypt(old_name)
    os.rename(file, name_decrypted)
        