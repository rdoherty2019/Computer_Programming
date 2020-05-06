"""
your_face.py

Richie Doherty
2/5/20
CSCI-UA.0003-002 Section 1
=====
Draw a face using turtle. For example, you can draw the look of disapproval!

![look of disapproval](http://foureyes.github.io/csci-ua.0002-fall2015-008/resources/img/turtle/your_face.png)

Requirements
-----

* you can draw whatever face you like
* but you have to use the turtle module
    * need some help drawing? (https://docs.python.org/3.7/library/turtle.html)
    * change the size of the pen 
    * set the window size to 400 x 400
    * hint: if you want your drawing to display faster, turn animation off
"""
#importing turtle
import turtle

#Make pen
t = turtle.Turtle()

#make a surface
wn = turtle.Screen()

#setting the screen size
wn.setup(400,400)

#Eyes

#Eye 1
t.up() #pick up the pen
t.goto(-75, 125) # Move pen
t.down() #put the pen down

#Setting circle eye color
t.color('black', 'black')
t.begin_fill()
t.circle(20)
t.end_fill()

#Eye 2
t.up()
t.goto(75, 125)
t.down()

#Setting circle eye color
t.color('black', 'black')
t.begin_fill()
t.circle(20)
t.end_fill()

#Nose
t.up() #pick up the pen
t.goto(-5, 5) # Move pen
t.down() #to put the pen down

#change size
t.pensize(10)

t.right(45)
t.forward(20)
t.right(90)
t.forward(20)
t.goto(-5, 5)

# Mouth
t.up()
t.goto(125, -150)
t.down()

t.right(90)
t.forward(75)
t.left(45)
t.forward(150)
t.left(45)
t.forward(75)


#Keeps drawing open
wn.mainloop()