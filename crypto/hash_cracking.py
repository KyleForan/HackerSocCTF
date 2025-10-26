import hashlib
import secrets

wordlist = open("wordlist.txt").read().splitlines()

word = secrets.choice(wordlist)
hashed = hashlib.md5(word.encode()).hexdigest()

print(f"Hashed: {hashed}")
# Hashed: adff44c5102fca279fce7559abf66fee