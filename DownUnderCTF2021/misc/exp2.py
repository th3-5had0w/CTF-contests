from PIL import Image


for j in range(0, 10):
    pos = 0
    ni = Image.new('RGB', (300, 22*12), (255, 255, 255))

    image0 = Image.open('frame_00'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_01'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_02'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_03'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_04'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_05'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_06'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_07'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_08'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_09'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_10'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    image0 = Image.open('frame_11'+str(j)+'_delay-0.05s.png')
    ni.paste(image0, (0, pos))
    pos+=21
    image0.close()
    name = "dat"+str(j)+".png"
    ni.save(name, "PNG")
    ni.close()