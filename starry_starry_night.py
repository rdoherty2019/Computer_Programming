import turtle

# pen
t = turtle.Turtle()

#name screen
wn = turtle.Screen()

#setting screen size to 600 h by 800 w
wn.setup(800,600)

#screen color
wn.bgcolor('black')

#pen color
t.color('yellow')

"""
#part 1
#drawing 1 star

#Move pen to starting point
t.up()
t.goto(-100,75)
t.down()

#Draw
t.goto(100, 75)

t.right(135)

t.goto(-100, -75)

t.right(135)

t.goto(0, 150)

t.right(135)

t.goto(100, -75)

t.right(135)

t.goto(-100,75)

"""
"""
#part 2
#Drawing several stars

#starting point
x = -800
y = 0

#Move pen to starting point
t.up()
t.goto(x, y)
t.down()

#Looping through drawing
while x < 800:
    #skipping first movement
    if x != -800:
        t.up()
        t.goto(x + 100, y)
        t.down()
    #nested loop to actually draw
    for i in range(16):
        t.goto(x + 100, y)

        t.right(135)

        t.goto(x, y - 100)

        t.right(135)

        t.goto(x + 50, y + 100)

        t.right(135)

        t.goto(x + 100 , y -100)

        t.right(135)

        t.goto(x , y)

        #adding on to conditional variable
        x += 100
"""

#part 3
import random

#looping for drawing 40 stars
for i in range(40):
    #setting random starting point
    #need two coordinates X & Y
    starting_x = random.randint(-800, 700)
    starting_y = random.randint(-500, 500)

    #Need to dimensions of the start
    distance = random.randint(10, 100)

    #moving to starting location
    t.up()
    t.goto(starting_x, starting_y)
    t.down()

#drawing
    t.goto(starting_x + distance, starting_y)

    t.right(135)

    t.goto(starting_x, starting_y - distance)

    t.right(135)

    t.goto(starting_x + distance/2, starting_y + distance)

    t.right(135)

    t.goto(starting_x + distance, starting_y - distance)

    t.right(135)

    t.goto(starting_x, starting_y)


#keep screen open
wn.mainloop()