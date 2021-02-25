'''Alex Vegso, 02/04/21. The code for the first one is supposed to make horizontal lines and vertical lines go forward until they connect with each other. The code for the second one is supposed to'''
def turtles_in_traffic_1():
    import turtle as trtl
    # makes two new, empty, lists
    horiz_turtles = []
    vert_turtles = []
    # made a list for the shapes, the horizontal colors, and the vertical colors
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
    vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
    # this variable is used to to calculate the turtles ending position
    tloc = 50

    # setsa forloop in which makes the shapes go to their starting positions 
    for s in turtle_shapes:
        ht = trtl.Turtle(shape=s)
        horiz_turtles.append(ht)
        ht.penup()
        new_color = horiz_colors.pop()
        ht.fillcolor(new_color)
        ht.goto(-350, tloc)
        ht.setheading(0)
        #
        vt = trtl.Turtle(shape=s)
        vert_turtles.append(vt)
        vt.penup()
        new_color = vert_colors.pop()
        vt.fillcolor(new_color)
        vt.goto( -tloc, 350)
        vt.setheading(270)
        #ads 50 to the x and y values in the starting positions
        tloc += 50
    # TODO: move turtles across and down screen, stopping for collisions
    steps = 0
    while steps < 50:
        for ht in horiz_turtles:
            for vt in vert_turtles:
                ht.forward(3)
                vt.forward(3)
                x_distance = abs(ht.xcor() - vt.xcor())
                y_distance = abs(ht.ycor() - vt.ycor())
                if (x_distance < 20):
                    if (y_distance < 20):
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)
        steps = steps + 1
    wn = trtl.Screen()
    wn.mainloop()


def turtles_in_traffic_2():
    import turtle as trtl
    # makes two new, empty, lists
    horiz_turtles = []
    vert_turtles = []
    # made a list for the shapes, the horizontal colors, and the vertical colors
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
    vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
    # this variable is used to to calculate the turtles ending position
    tloc = 50

    # setsa forloop in which makes the shapes go to their starting positions 
    for s in turtle_shapes:
        ht = trtl.Turtle(shape=s)
        horiz_turtles.append(ht)
        ht.penup()
        new_color = horiz_colors.pop()
        ht.fillcolor(new_color)
        ht.pencolor(new_color)
        ht.goto(-350, tloc)
        ht.setheading(0)
        ht.pendown()
        ht.speed(0)
        #
        vt = trtl.Turtle(shape=s)
        vert_turtles.append(vt)
        vt.penup()
        new_color = vert_colors.pop()
        vt.fillcolor(new_color)
        vt.pencolor(new_color)
        vt.goto( -tloc, 350)
        vt.setheading(270)
        vt.pendown()
        vt.speed(0)
        #ads 50 to the x and y values in the starting positions
        tloc += 50
    # move turtles across and down screen with lines, then with half circles, stopping when it is 20 pixels too close to each other
    steps = 0
    while steps < 50:
        for ht in horiz_turtles:
            for vt in vert_turtles:
                ht.forward(3)
                ht.left(270)
                ht.circle(3,-180)
                ht.left(270)
                vt.forward(3)
                vt.left(270)
                vt.circle(3,-180)
                vt.left(270)
                x_distance = abs(ht.xcor() - vt.xcor())
                y_distance = abs(ht.ycor() - vt.ycor())
                if (x_distance < 20):
                    if (y_distance < 20):
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)
        steps = steps + 1
    wn = trtl.Screen()
    wn.mainloop()


def turtles_in_traffic_3():
    import turtle as trtl
    # makes two new, empty, lists
    horiz_turtles = []
    vert_turtles = []
    # made a list for the shapes, the horizontal colors, and the vertical colors
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
    vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
    # this variable is used to to calculate the turtles ending position
    tloc = 50

    # setsa forloop in which makes the shapes go to their starting positions 
    for s in turtle_shapes:
        ht = trtl.Turtle(shape=s)
        horiz_turtles.append(ht)
        ht.penup()
        new_color = horiz_colors.pop()
        ht.fillcolor(new_color)
        ht.pencolor(new_color)
        ht.goto(-350, tloc)
        ht.setheading(0)
        ht.pendown()
        ht.speed(0)
        #
        vt = trtl.Turtle(shape=s)
        vert_turtles.append(vt)
        vt.penup()
        new_color = vert_colors.pop()
        vt.fillcolor(new_color)
        vt.pencolor(new_color)
        vt.goto( -tloc, 350)
        vt.setheading(270)
        vt.pendown()
        vt.speed(0)
        #ads 50 to the x and y values in the starting positions
        tloc += 50
    # move turtles across and down screen with lines, then with half circles, stopping when it is 20 pixels too close to each other
    steps = 0
    while steps < 50:
        for ht in horiz_turtles:
            for vt in vert_turtles:
                ht.circle(3,-360)
                ht.forward(3)
                vt.circle(3,-360)
                vt.forward(3)
                x_distance = abs(ht.xcor() - vt.xcor())
                y_distance = abs(ht.ycor() - vt.ycor())
                if (x_distance < 20):
                    if (y_distance < 20):
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)
        steps = steps + 1
    wn = trtl.Screen()
    wn.mainloop()


function_chooser = int(input("Which function do you want to use? (1 or 2 or 3) "))
if (function_chooser == 1):
    turtles_in_traffic_1()
elif (function_chooser == 2):
    turtles_in_traffic_2()
elif (function_chooser == 3):
    turtles_in_traffic_3()
else: 
  print("Function not defined")