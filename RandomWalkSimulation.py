from drawingpanel import *
import random
import math
import time
panel = DrawingPanel(1080, 720)
panel.set_background("white")
direction=["right","left","up","down"]
x0=400
y0=400
x1=420
y1=400
event=""
counter=0
for i in range(0,5000,5):
    
    randomnumber=random.randint(0,3)
    if event!="left" and event!="right" and direction[randomnumber]=="right":
        if (x1+i)+20> 1080:
            continue
        else:
            counter+=1
            time.sleep(1)
            panel.canvas.create_line(x0,y0,x1+i,y1,fill="black")
            x0=x1+i
            y0=y1
            x1=x1+i
            event="right"
            panel.sleep(10)
        
    elif event!="right" and event!="left" and direction[randomnumber]=="left":
        if (x1-i)-20<0:
            continue
        else:
            counter+=1
            time.sleep(1)
            panel.canvas.create_line(x0,y0,x1-i,y1,fill="black")
            x0=x1-i
            y0=y1
            x1=x1-i
            event="left"
            panel.sleep(10)
    elif event!="down" and event!="up" and direction[randomnumber]=="up":
        if (y1+i)+20> 720:
            continue
        else:
            counter+=1
            time.sleep(1)
            panel.canvas.create_line(x0,y0,x1,y1+i,fill="black")
            x0=x1
            y0=y1+i
            y1=y1+i
            event="up"
            panel.sleep(10)
    elif event!="up" and event!="down" and direction[randomnumber]=="down":
        if (y1-i)-20<0:
            continue
        else:
            counter+=1
            time.sleep(1)
            panel.canvas.create_line(x0,y0,x1,y1-i,fill="black")
            x0=x1
            y0=y1-i
            y1=y1-i
            event="down"
            panel.sleep(10)        

    else:
        continue

print(counter)


