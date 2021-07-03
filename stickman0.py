import turtle as td
from turtle import Turtle as turt

z = -1

wn = td.Screen()
bob = turt()

butt = bob.pos()

bob.rt(-90)
bob.fd(100)
neck = bob.pos()

bob.seth(180+15)
bob.fd(35)
l_sho = bob.pos()
r_sho = ( bob.xcor()*z, bob.ycor() )

bob.pu()
bob.goto(neck)
bob.pd()

bob.goto(r_sho)

wn.mainloop()