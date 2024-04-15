from idc      import *
from idaapi   import *
from idautils import *

#bp in main

addr = 0x40214C

def print_horizon_wall(horizon_wall, trap,x):
    result = print("|",end = "")
    for i in range(12):
        if ( horizon_wall[i] ):
            wall = '|'
        else:
            wall = ' '
        if i==x:
            obj = 'o'
        elif ( trap[i*4] ):
            obj = '*'
        else:
            obj = ' '
        print("%c%c"%(obj, wall),end = "")

def print_vertical_wall(vertical_wall):
    for i in range(12):
        if vertical_wall[i]:
            v1 = '-'
        else:
            v1 = ' '
        print(f"+{v1}",end = "")
    print('+')

def print_maze():
    HORIZON = idaapi.get_dword(0x415044)
    VERTICAL =  idaapi.get_dword(0x415040)
    TRAP = 0x415060
    print(get_reg_value("eip"))
    curx = idaapi.get_dword(idaapi.get_dword(get_reg_value("ebp")-0x1c))
    cury = idaapi.get_dword(idaapi.get_dword(get_reg_value("ebp")-0x1c)+4)
    print(curx,cury)
    print("+-"*12 + "+")
    for i in range(12):
        if i==cury:
            x = curx
        else:
            x = -1
        # print(hex(HORIZON),hex(VERTICAL))
        print_horizon_wall(get_bytes(HORIZON+i*12,12),get_bytes(TRAP+i*12*4,12*4),x)
        print()
        print_vertical_wall(get_bytes(VERTICAL+i*12,12))
    print("                       H")



# See idapython/src/examples/debughook.py
class MyDbgHook(DBG_Hooks):
    def dbg_bpt(self, tid, ea):
        print("Break point at 0x%x pid=%d" % (ea, tid))
        # return values:
        #   -1 - to display a breakpoint warning dialog
        #        if the process is suspended.
        #    0 - to never display a breakpoint warning dialog.
        #    1 - to always display a breakpoint warning dialog.
        global addr
        if (ea == addr):
            print_maze()
        return 0

    def dbg_process_exit(self, pid, tid, ea, code):
        print("Process exited pid=%d tid=%d ea=0x%x code=%d" % (pid,
            tid, ea, code))
        # xs = sorted(lst, key=lambda x: x[1], reverse=True)[0:3]
        global lst
        
        xs = sorted(lst, key=lambda x: x[1])
        map(lambda x: Message("%s\n" % str(x)), xs)

# Add breakpoint.
idc.add_bpt(addr)

# Remove an existing debug hook
try:
    if debughook:
        print("Removing previous hook ...")
        debughook.unhook()
except:
    pass

# Install the debug hook
debughook = MyDbgHook()
debughook.hook()

# Stop at the entry point
ep = 0x40192C
request_run_to(ep)

# Step one instruction
request_step_over()

# Start debugging
run_requests()
