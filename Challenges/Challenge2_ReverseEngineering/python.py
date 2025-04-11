# I used ChatGpt to generate most of this code

import hashlib
from itertools import product

target_hash = "5b3903fb58dc5fcd7a3f88c7fae3994b151a6bfb90e8a808dced034ca6bc9910"

# Loads top 100 passwords from file
with open("10-million-password-list-top-100.txt", "r", encoding="utf-8") as f:
    passwords = [line.strip() for line in f.readlines() if line.strip()]

for pw1, pw2 in product(passwords, repeat=2):
    for num in range(100):
        middle = f"{num:02d}"
        combo = pw1 + middle + pw2
        hashed = hashlib.sha256(combo.encode()).hexdigest()
        
        if hashed == target_hash:
            print(f"[+] Match found!")
            print(f"    Password 1: {pw1}")
            print(f"    Number    : {middle}")
            print(f"    Password 2: {pw2}")
            print(f"    Full Combo: {combo}")
            exit()

print("[-] No match found.")
