text = input("What would you like to encrypt?: ")
letters = "abcdefghjklmnopqrstuvwxyz"
count = 1
cipher = ""

for i in text:
    if i in letters:
        cipher += letters [(letters.index (i) + count) % (len(letters))]

print(f"Encrypted message: {cipher}")
