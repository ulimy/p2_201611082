import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.penup()
t2.setpos(-50,100)
t2.pendown()
t2.forward(100)
def keyup():
    t1.forward(50)
def keydown():
    t1.backward(50)
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y) 
    if -50<x<50 and 95<y<105:
        print ("Correct")
def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
def addmouse():
    wn.onclick(mousegoto)
addkeys()
addmouse() 
wn.listen()
turtle.mainloop()
