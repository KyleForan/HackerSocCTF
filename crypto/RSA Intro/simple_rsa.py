from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

FLAG = b"EHS{FAKE_FLAG}"
m = bytes_to_long(FLAG)

p, q = getPrime(1024), getPrime(1024)
n = p*q

e = 0x10001
c = pow(m, e, n)
tot = (p-1) * (q-1)

print(f'{n = }') 
print(f'{tot = }')
print(f'{e = }')

print(f"Ciphertext: {c}")
