import os

os.system('convert challenge.gif qr.jpg')

for i in range(0, 10):
    same_color = ''
    for j in range(i, 120, 10):
        same_color += f'qr-{j}.jpg '

    os.system(f'convert {same_color} -append ans{i}.jpg')
