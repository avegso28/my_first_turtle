def code_stem_1 ():
    import turtle as trtl 
    bob = trtl.Turtle()
    bob.speed(0)
    bob.penup()
    bob.goto(-150,5)
    bob.shape("square")
    bob.color("salmon")

    line = 6

    while (line > 5):
        bob.pendown()
        bob.circle(5)
        bob.penup()
        bob.forward(20)
        line += 1

    window = trtl.Screen()
    window.exitonclick()


def code_stem_2():
    j = 0
    while (j < 10):
        print("j: ", j)
        j += 1

        d = 0
        while (d < 5): 
            print(" d: ", d)
            d += 1

            b = 0
            while (b < 4):
                print("  b: ", b)
                b += 1


def code_stem_3():
    import turtle as trtl 
    logan = trtl.Turtle()
    logan.shape("circle")
    logan.hideturtle()
    logan.penup()

    x = -200
    while (x < 200):
        x += 50
        y = 200
        logan.goto(x, y)
        logan.color("red")
        logan.stamp()

        while (y > 0):
            y -= 50
            logan.goto(x, y)
            logan.color("blue")
            logan.stamp()

    window = trtl.Screen()
    window.exitonclick()

def code_stem_4():
    import turtle as trtl 
    logan = trtl.Turtle()
    logan.shape("circle")
    logan.hideturtle()
    logan.penup()

    y = 200
    while (y > -200):
        y -= 50
        x = -300
        logan.goto(x, y)
        logan.color("blue")
        logan.stamp()

        while (x <= 50) and (x > -350):
            x += 50
            logan.goto(x, y)
            logan.color("yellow")
            logan.stamp()

    window = trtl.Screen()
    window.exitonclick()


code_stem = input("Which code stem do you want to run? ")

if (code_stem == "1"):
    code_stem_1()
elif (code_stem == "2"):
    code_stem_2()
elif (code_stem == "3"):
    code_stem_3()
elif (code_stem == "4"):
    code_stem_4()