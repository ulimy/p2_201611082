﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareAtSave(size, pos):
    t1.penup() 
    t1.setpos(pos) 
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks

def drawSquareFrom():
    t1.pendown()
    tracks=((0,0), (100,0), (100,-100), (0,-100), (0,0))
    for i in range(0,5):
        t1.goto(tracks[i])
    return tracks

def lab7b():
    mytrack1=drawSquareAtSave(100,(0,0))
    print (mytrack1)

def lab7c():
    mytrack2=drawSquareFrom()

def main():
    lab7b()
    lab7c()
    
if _name_=="_main_":
    main()
