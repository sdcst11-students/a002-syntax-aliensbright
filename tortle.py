import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("blue")
t.penup()
t.color("black","#39e75f")
t.begin_fill()
t.goto(200,0)
t.pensize(7)
t.pendown()
t.goto(200,20)
t.goto(150,30)
t.goto(125,-10)
t.goto(80,-10)
t.goto(100,-40)
t.goto(135,-40)
t.goto(125,-10)
t.goto(180,-20)
t.goto(200,0)
t.end_fill()
t.penup()
t.goto(0,-20)
t.pensize(10)
t.begin_fill()
t.pendown()
t.pensize(7)
t.goto(50,-70)
t.goto(50,-90)
t.goto(0,-90)
t.goto(-80,-10)
t.goto(-50,-60) 
t.goto(-70,-60)

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS H:\Documents\GitHub\a002-syntax-aliensbright> py   
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> s = turtle.getscreen()
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> t.penup()
>>> t.color("#5C4033","#39e75f")
>>> t.begin_fill()
>>> t.goto(200,0)
>>> t.pensize(10)
>>> t.pendown()
>>> t.goto(200,20)
>>> t.goto(125,-10)
>>> t.goto(80,-10)
>>> t.goto(100,-40)
>>> t.goto(135,-40)
>>> t.goto(125,-10)
>>> t.goto(180,-20)
>>> t.goto(200,0)
>>> t.end_fill()
>>> t.penup
PS H:\Documents\GitHub\a002-syntax-aliensbright> py
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> s = turtle.getscreen()
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> turtle.bgcolor("blue")
>>> t.penup()
>>> t.color("black","#39e75f")
>>> t.begin_fill()
>>> t.goto(200,0)
>>> t.pensize(7)
>>> t.pendown()
>>> t.goto(200,20)
>>> t.goto(150,30)
>>> t.goto(125,-10)
>>> t.goto(80,-10)
>>> t.goto(100,-40)
>>> t.goto(135,-40)
>>> t.goto(125,-10)
>>> t.goto(180,-20)
>>> t.goto(200,0)
>>> t.end_fill()
>>> t.penup()
>>> t.goto(0,-20)
>>> t.pensize(10)
>>> t.begin_fill()
>>> t.pendown()
>>> t.pensize(7)
>>> t.goto(50,-70)
>>> t.goto(50,-90)
>>> t.goto(0,-90)
>>> t.goto(-80,-10)
>>> t.goto(-50,-60)
>>> t.undo()
>>> t.goto(-45,-60)
>>> t.goto(-70,-80
... )
>>> t.goto(-75,-80)
>>> t.goto(-80,-20)
>>> t.undo()
>>> t.goto(-100,-30)
>>> t.undo()
>>> t.goto(-120,0)
>>> t.goto(-80,-10)
>>> t.goto(-120,0)
>>> t.goto(190,0)
>>> t.undo()
>>> t.goto(-190,0)
>>> t.goto(-210,30)
>>> 