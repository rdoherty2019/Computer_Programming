import turtle
t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

# set the width and height of our screen
width, height = 500, 500
wn.setup(width, height)

#defining function
def get_quadrant_color(click_x, click_y):

    #Starting criteria
    if click_x == 0 and click_y == 0:
        return 'red'

    elif click_x >= 0 and click_y >= 0:
        return 'red'
    elif click_x <= 0 and click_y >= 0:
        return  'blue'
    elif click_x <= 0 and click_y <= 0:
        return 'yellow'
    elif click_x >=0 and click_y <=0:
        return 'green'


def handle_click(x, y):
    # pick your pen up
    # =====================================
    t.up()

    # move your turtle to the x and y coordinates that are the parameters
    # of this function
    # =====================================
    t.goto(x, y)

    # put your pen back down
    # =====================================
    t.down()

    # call your get_quadrant_color function here and save save the result
    # in a variable called quadrant_color
    # =====================================
    quadrant_color = get_quadrant_color(x, y)

    # set the turtle's drawing color to the quadrant_color variable that
    # you created above
    # =====================================
    t.color(quadrant_color)

    # draw a filled circle by calling the following methods on your
    # *turtle object* in order:
    #
    # begin_fill()
    # circle() <--- circle has radius as a parameter
    # end_fill()
    # =====================================
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# when the screen is clicked, call the handle_click function (and pass it the
# x and y coordinates
wn.onclick(handle_click)

wn.mainloop()