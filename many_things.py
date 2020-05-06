"""
many_things.py

Richie Doherty
=====

Create a turtle program that draws multiple objects

* It should use a list of dictionaries to define the properties of each
  object in your drawing.
* There should be at least 10 different objects in different locations on
  the screen.
* For example, you can draw multiple trees (simply a rectangle and triangle)
  ...and the dictionary would have keys that may represent:
  * the tree's total height
  * the x and y coordinate

Create any drawing you like! As long as the drawing uses the list of
dictionaries as the basis of where/how things are drawn.
"""
import turtle
t = turtle.Turtle()
w = turtle.Screen()

w.setup(1000,1000)

draw = [{"height": 50, "Location" : [-290,-240]},
        {"height": 50, "Location" : [-230,-180]},
        {"height": 50, "Location" : [-170,-120]},
        {"height": 50, "Location" : [-110,-60]},
        {"height": 50, "Location" : [0,50]},
        {"height": 50, "Location" : [60,110]},
        {"height": 50, "Location" : [120,170]},
        {"height": 50, "Location" : [180,230]},
        {"height": 50, "Location" : [240,290]},
        {"height": 50, "Location" : [300,350]}
        ]

#looping for drawing
for i in range(len(draw)):

    #need two coordinates X & Y
    starting_x = draw[i]["Location"][0]
    starting_y = draw[i]["Location"][1]

    #Need to dimensions of the tree
    distance = draw[i]["height"]

    #moving to starting location
    t.up()
    t.goto(starting_x, starting_y)
    t.down()

#drawing

    # base
    t.goto(starting_x , starting_y+ distance/2)

    t.right(90)

    t.goto(starting_x + distance /2, starting_y + distance /2 )

    t.right(90)

    t.goto(starting_x + distance/2, starting_y )

    t.right(90)

    t.goto(starting_x , starting_y )

    #branches
    t.up()
    t.goto(starting_x - distance/4, starting_y + distance /2)
    t.down()

    t.right(45)

    t.goto(starting_x + distance/4, starting_y + distance)

    t.right(45)

    t.goto(starting_x + 3 * (distance / 4), starting_y + distance / 2)

    t.right(45)

    t.goto(starting_x - distance / 4, starting_y + distance / 2)

#keep screen open
w.mainloop()
