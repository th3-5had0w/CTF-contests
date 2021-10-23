from z3 import *
from pwn import *

a = open('flag.png.encrypted', 'rb').read()
data_len = len(a)//2
arr= []

for i in range(data_len):
    encrypted = u16(chr(a[i*2])+chr(a[i*2+1]))
    s = Solver()
    state = BitVec('state', 64)
    print(type(state))
    s.add(encrypted == 21727 * (18199 * ((25561 * (31663 * (0xF99D * (state ^ 0x6BB1) - 0x3F44) + 14122)) ^ 0x448C) - 11258))
    s.check()
    state = s.model()[state]
    print(type(state))
    for j in range(0x20F76D1):
        s = Solver()
        prev_state = BitVec('prev_state', 64)
        s.add(state == 21727 * (18199 * ((25561 * (31663 * (0xF99D * (prev_state ^ 0x6BB1) - 0x3F44) + 14122)) ^ 0x448C) - 11258))
        s.check()
        state = s.model()[prev_state]

    arr.append(s.model()[prev_state])

print(arr)
