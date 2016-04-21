import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("Red")
width=wn.window_width()
height=wn.window_height()
a0=int(30-(width/2))
a1=int(a0+((width-60)/3))
a2=int(a1+((width-60)/3))
a3=int((width/2)-30)
b0=int(30-(height/2))
b1=int(b0+((height-60)/3))
b2=int(b1+((height-60)/3))
b3=int((height/2)-30)
treasure=list()
import random
x1=random.randrange(a0,a1)
y1=random.randrange(b0,b1)
y2=random.randrange(b1,b2)
y3=random.randrange(b2,b3)
treasure.append((x1,y1))
treasure.append((x1,y2))
treasure.append((x1,y3))
import random
x2=random.randrange(a1,a2)
y1=random.randrange(b0,b1)
y3=random.randrange(b2,b3)
treasure.append((x2,y1))
treasure.append((x2,y3))
import random
x3=random.randrange(a2,a3)
y1=random.randrange(b0,b1)
y2=random.randrange(b1,b2)
y3=random.randrange(b2,b3)
treasure.append((x3,y1))
treasure.append((x3,y2))
treasure.append((x3,y3))
for i in range(0,8):
    t1.penup()
    t1.goto(treasure[i])
    t1.circle(30)
    t1.home()
x=400
y=400
while (x<-350 or x>350) or (y<-350 or y>350):
    print ("-350<=x&y<=350")
    x1=input("Where would you like to go?(width):")
    y1=input("Where would you like to go?(height):")
    x=int(x1)
    y=int(y1)
t1.goto(x,y)
for i in range(0,6):
    if (x,y)==treasure[i]:
        t1.pendown()
        t1.pencolor("Blue")
        t1.circle(30)
    else:
        t1.home()  