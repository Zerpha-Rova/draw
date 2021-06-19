import turtle as td
from turtle import Turtle as ttl
z= -1

wn = td.Screen() 
wn.colormode(255)
bob = ttl()
tim = ttl()
bob.speed(10)
tim.speed(10)

def fxn(x, y): #onclick (x, y) ends up here
	bob.pd()
	if y < bob.ycor():
		bob.pencolor((250,10,10))
	else:
		bob.pencolor((10,10,250))
	bob.goto(x, y) 
	bob.up()
	if x <= tim.xcor():
		tim.pencolor((10,250,10))
	else:
		tim.pencolor((250,10,250))
	tim.down()
	tim.goto(x*z,y*z)
	tim.pu()

bob.up()
tim.penup()

# onclick passes click (x,y)
wn.onclick(fxn) 

wn.mainloop()