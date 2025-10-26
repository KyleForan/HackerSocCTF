import pwn

FLAG = "EHS{FAKE_FLAG}"
KEY = "SUPER_SECURE"

def xor(string, key):
    key = key[:len(string)]
    output = b''

    for i in range(len(string)):
        output += chr(ord(string[i]) ^ ord(key[i % len(key)])).encode()
    
    return output

enc = xor(FLAG, KEY)
print(enc)