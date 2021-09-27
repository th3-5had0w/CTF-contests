from tkinter import *

fp = open('flate.txt', 'r')

for i in range(7):
    print(fp.readline())

root = Tk()
root.title("BRUH")
cw = 1200
ch = 800

canvas_1 = Canvas(root, height=ch, width=cw, background='white')
canvas_1.grid(row=0, column=1)

zoom_factor_x = 4.25
zoom_factor_y = 4
x_offset = 180
y_offset = 400
x_prev = 0
y_prev = 0

while (True):
    cmd = fp.readline().split()
    if (cmd[-1] == 'm'):
        x_prev = (float(cmd[0]) - x_offset) * zoom_factor_x
        y_prev = (float(cmd[1]) - y_offset) * zoom_factor_y

    if cmd[-1] == 'l':
        x_coord = (float(cmd[0]) - x_offset) * zoom_factor_x
        y_coord = (float(cmd[1]) - y_offset) * zoom_factor_y
        canvas_1.create_line(x_prev, ch-y_prev, x_coord, ch-y_coord)

    if cmd[-1] == 'c':
        x1 = (float(cmd[0]) - x_offset) * zoom_factor_x
        y1 = (float(cmd[1]) - y_offset) * zoom_factor_y
        x2 = (float(cmd[2]) - x_offset) * zoom_factor_x
        y2 = (float(cmd[3]) - y_offset) * zoom_factor_y
        x3 = (float(cmd[4]) - x_offset) * zoom_factor_x
        y3 = (float(cmd[5]) - y_offset) * zoom_factor_y
        x_prev = x3
        y_prev = y3
        canvas_1.create_line(x1, ch-y1, x2, ch-y2, x3, ch-y3, smooth="true")

    if 'n' in cmd[-1]:
        continue
    if 'f*' in cmd[-1]:
        continue


root.mainloop()
