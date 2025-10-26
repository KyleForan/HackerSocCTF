from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

FLAG = b"EHS{FAKE_FLAG}"
m = bytes_to_long(FLAG)

p, q = getPrime(256), getPrime(256)
n = p*q

e = 0x10001
c = pow(m, e, n)

print(f'{n = }') 
print(f'{e = }')

print(f"Ciphertext: {c}")
