import angr
import claripy

flag_len = 22
flag = claripy.BVS("flag", 8*flag_len)



pro = angr.Project('./alien_math', main_opts = {"base_addr":0}, auto_load_libs = False)

state = pro.factory.full_init_state(args=[pro.filename], add_options=angr.options.unicorn, remove_options={angr.options.LAZY_SOLVES})

simu = pro.factory.simulation_manager(state)

simu.explore(find=0x40129a)

print(simu.found[0].posix.dumps(0))
