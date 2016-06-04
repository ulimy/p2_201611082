treasure2=list()
d=list()
import turtle
import time
wn=turtle.Screen()
wn.bgcolor("Black")
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("Blue")

def DecideTreasure(treasure2):
    width=wn.window_width()
    height=wn.window_height()
    treasure1=list()
    a0=int(30-(width/2))
    a1=int(a0+((width-60)/3))
    a2=int(a1+((width-60)/3))
    a3=int((width/2)-30)
    b0=int(30-(height/2))
    b1=int(b0+((height-60)/3))
    b2=int(b1+((height-60)/3))
    b3=int((height/2)-30)
    import random
    x1=random.randrange(a0,a1)
    y1=random.randrange(b0,b1)
    y2=random.randrange(b1,b2)
    y3=random.randrange(b2,b3)
    treasure1.append((x1,y1))
    treasure1.append((x1,y2))
    treasure1.append((x1,y3))
    import random
    x2=random.randrange(a1,a2)
    y1=random.randrange(b0,b1)
    y3=random.randrange(b2,b3)
    treasure1.append((x2,y1))
    treasure1.append((x2,y3))
    import random
    x3=random.randrange(a2,a3)
    y1=random.randrange(b0,b1)
    y2=random.randrange(b1,b2)
    y3=random.randrange(b2,b3)
    treasure1.append((x3,y1))
    treasure1.append((x3,y2))
    treasure1.append((x3,y3))
    for i in treasure1:
        treasure2.append((i[0],i[1]+30))
    for i in range(0,8):
        t1.penup()
        t1.speed(10)
        t1.goto(treasure1[i])
        t1.pendown()
        t1.circle(30)
    t1.penup()
    t1.home()
    t1.clear()

def FindTreasure(treasure2,x,y,d):
    import math
    for i in treasure2:
        distance1=math.pow((x-i[0]),2)+math.pow((y-i[1]),2)
        distance2=math.sqrt(distance1)
        d.append(distance2)
        if distance2<=30:
            wn.bgcolor("Black")
            t1.penup()
            t1.goto(i[0],i[1]-30)
            t1.setheading(0)
            t1.color("Green")
            t1.pendown()
            t1.fillcolor("Green")
            t1.begin_fill()
            t1.circle(30)
            t1.end_fill()
            t1.penup()
            t1.color("Blue")
            t1.home()
    if (30<d[0]<=55) or (30<d[1]<=55) or (30<d[2]<=55) or (30<d[3]<=55) or (30<d[4]<=55) or (30<d[5]<=55) or (30<d[6]<=55) or (30<d[7]<=55):
        wn.bgcolor("Red")
    elif (55<d[0]<=80) or (55<d[1]<=80) or (55<d[2]<=80) or (55<d[3]<=80) or (55<d[4]<=80) or (55<d[5]<=80) or (55<d[6]<=80) or (55<d[7]<=80):
        wn.bgcolor("Yellow")
    else:
        wn.bgcolor("Black")

def keyup():
    t1.forward(10)
    x=t1.pos()[0]
    y=t1.pos()[1]
    FindTreasure(treasure2,x,y,d)
    t1.penup()

def keydown():
    t1.backward(10)
    x=t1.pos()[0]
    y=t1.pos()[1]
    FindTreasure(treasure2,x,y,d)
    t1.penup()

def keyright():
    t1.right(45)

def keyleft():
    t1.left(45)

def game():
    DecideTreasure(treasure2)
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
    wn.listen()
    turtle.mainloop()

def gamePlay():
    guessTaken=0
    file1=open('Time.txt',w)
    file1.write(time.strftime('%Y-%m-%d %H:%M:%S'))
    file1.close()
    game()
    while guessTaken<5:
        guessTaken=guessTaken+1
        file2=open('Time.txt',a)
        file2.write("\n"+time.strftime('%Y-%m-%d %H:%M:%S'))
        game()
    file2.close()

def main():
    gamePlay()    

if __name__=="__main__": 
     main()  
