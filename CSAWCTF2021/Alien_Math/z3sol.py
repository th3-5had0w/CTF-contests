import angr
import claripy

project = angr.Project('./alien_math')

key_len = 22
flag = claripy.BVS("flag", 8*22)

state = project.factory.entry_state(stdin = flag)

state.solver.add(flag.get_byte(0) == 7)

for i in range(key_len):
    state.solver.add(flag.get_byte(i) > 47)
    state.solver.add(flag.get_byte(i) <= 57)

for i in range(key_len-1):

