FLAG = b"EHS{FAKE_FLAG}"
KEY = b"SUPER_SECURE"

def xor(string, key):
    key = key[:len(string)]
    output = b''

    for i in range(len(string)):
        output += chr(string[i] ^ key[i % len(key)]).encode()
    
    return output

enc = xor(FLAG, KEY)
print(enc)

# enc = b'\x16\x1d\x03>\n\x10\x01\x1a\n\x06\r\x17\x16\x03\x15\x17\x01\x1e\x11\t\x06('