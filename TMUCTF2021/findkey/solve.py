import angr
import claripy

project = angr.Project('./findkey')

key_len = 16
key = claripy.BVS("key", 8*key_len)
v6 = claripy.BVS("v6", 32)
v7 = claripy.BVS("v7", 32)
v8 = claripy.BVS("v8", 32)
v9 = claripy.BVS("v9", 32)
v27 = claripy.BVS("v27", 32)
v26 = claripy.BVS("v26", 32)
v25 = claripy.BVS("v25", 32)
v24 = claripy.BVS("v24", 32)
v23 = claripy.BVS("v23", 32)
v22 = claripy.BVS("v22", 32)
v21 = claripy.BVS("v21", 32)
v20 = claripy.BVS("v20", 32)
v19 = claripy.BVS("v19", 32)
v18 = claripy.BVS("v18", 32)
v17 = claripy.BVS("v17", 32)
v16 = claripy.BVS("v16", 32)
v15 = claripy.BVS("v15", 32)
v14 = claripy.BVS("v14", 32)
v13 = claripy.BVS("v13", 32)
v12 = claripy.BVS("v12", 32)
v11 = claripy.BVS("v11", 32)
v10 = claripy.BVS("v10", 32)
v_arr = []
v_arr.append(v6)
v_arr.append(v7)
v_arr.append(v8)
v_arr.append(v9)

state = project.factory.entry_state(stdin = key)


for i in range(key_len // 4):
    state.solver.add(v_arr[i] == (((((key.get_byte(4 * i + 3) << 8) + key.get_byte(4 * i + 2)) << 8) + key.get_byte(4 * i + 1)) << 8) + key.get_byte(4 * i))



state.solver.add(v27 == (((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6)
state.solver.add(v26 == v27 ^ (v27 << 7))
state.solver.add(v25 == (v26 >> 1) + v26)
state.solver.add(v24 == v25 ^ (((v25 >> 3) & 0x20000000) + 32 * v25))
state.solver.add(v23 == (((v7 >> 3) & 0x20000000) + 32 * v7) ^ v7)
state.solver.add(v22 == v23 ^ (v23 << 7))
state.solver.add(v21 == (v22 >> 1) + v22)
state.solver.add(v20 == v21 ^ (((v21 >> 3) & 0x20000000) + 32 * v21))
state.solver.add(v19 == (((v8 >> 3) & 0x20000000) + 32 * v8) ^ v8)
state.solver.add(v18 == v19 ^ (v19 << 7))
state.solver.add(v17 == (v18 >> 1) + v18)
state.solver.add(v16 == v17 ^ (((v17 >> 3) & 0x20000000) + 32 * v17))
state.solver.add(v15 == (((v9 >> 3) & 0x20000000) + 32 * v9) ^ v9)
state.solver.add(v14 == v15 ^ (v15 << 7))
state.solver.add(v13 == (v14 >> 1) + v14)
state.solver.add(v12 == v13 ^ (((v13 >> 3) & 0x20000000) + 32 * v13))
state.solver.add(v11 == v20 ^ (v20 << 7))
((v20 ^ (v20 << 7)) >> 1) + (v20 ^ (v20 << 7)) == -231060518




v5[0] == v25 ^ (((((unsigned __int8)((((((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6) ^ (((((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6) << 7)) >> 1) + (v27 ^ (v27 << 7))) >> 3) & 0x20000000) + 32 * ((unsigned __int8)((v27 ^ (v27 << 7)) >> 1) + (((((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6) ^ (((((v6 >> 3) & 0x20000000) + 32 * v6) ^ v6) << 7))))

v5[1] == v20

v5[2] == v16

v5[3] == v12














v4[1] == -231060518



v4[2] == -706026796



4 * (v4[0] - 176506699) + 2 * (2 * v4[3] + 2 * v4[0]) == -966590128




2 * (2 * v4[3] + 2 * v4[0]) + v4[0] == -467021804




(2 * v4[3] + 2 * v4[0]) == 1163735118
