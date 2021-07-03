import turtle as td
from turtle import Turtle as turt

z = -1

wn = td.Screen()
bob = turt()

def line(a,b): ###a=(x1, y1) b=(x2,y2)
	bob.penup()
	bob.goto(a)
	bob.pendown()
	bob.goto(b)
	bob.penup()

line((70,-50),(110,55))
q = 66
w = (q, q*z)
v = (q*z, q)
line(w,v)


wn.mainloop()