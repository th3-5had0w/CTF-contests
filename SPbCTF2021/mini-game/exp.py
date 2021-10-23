from pwn import *
import socket
import paramiko

#io = process('./minigame')
io = ssh(host='142.93.131.0', user='minigame', password='openserver', port=2222)
