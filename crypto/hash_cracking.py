import hashlib
import secrets
from pwn import xor # temp

wordlist = open("wordlist.txt").read().splitlines()

FLAG = b"EHS{FAKE_FLAG}"

word = secrets.choice(wordlist)
hashed = hashlib.md5(word.encode()).hexdigest()


