import random
import base64
import codecs

FLAG = "EHS{FAKE_FLAG}"

def to_binary(in_str):
    output = ''

    for i in in_str:
        output += f'{ord(i):08b} '

    return output[:-1]

def to_hex(in_str):
    output = ''

    for i in in_str:
        output += f'{ord(i):02x} '

    return output[:-1]

def to_octal(in_str):
    output = ''

    for i in in_str:
        output += f'{ord(i):03o} '

    return output[:-1]

def to_base64(in_str):
    return base64.b64encode(
        in_str.encode()
    ).decode()

def ROT13(in_str):
    return codecs.encode(in_str, 'rot_13')

def main():
    print("The Flag has been encoded 5 times in a random order")
    print("Here are the encodings: Base64, Hex, Binary, Octal and ROT13")

    encodings = [to_base64, to_hex, to_binary, to_octal, ROT13]
    random.shuffle(encodings)

    enc = FLAG
    for func in encodings:
        enc = func(enc)
    print(f'\nEncoded Flag: {enc}')

if __name__ == '__main__':
    main()