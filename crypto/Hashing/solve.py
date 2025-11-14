import hashlib
import secrets

wordlist = open("wordlist.txt").read().splitlines()
hashed_flag = "adff44c5102fca279fce7559abf66fee"

# word = secrets.choice(wordlist)
for word in wordlist:
    hashed = hashlib.md5(word.encode()).hexdigest()
    if hashed == hashed_flag: 
        print('FLAG: EHS{' + word + '}')

print(f"Hashed: {hashed}")