import turtle as trtl
font_setup = ("Arial", 20, "normal")

triangle = trtl.Turtle()
triangle.penup()
triangle.backward(200)
triangle.pendown()
triangle.forward(40)
triangle.left(143.13)
triangle.forward(50)
triangle.left(126.87)
triangle.forward(30)
writer_1 = trtl.Turtle()
writer_2 = trtl.Turtle()
writer_2.penup()
writer_2.right(270)
writer_2.backward(25)
writer_2.right(90)
writer_2.pendown()
writer_3 = trtl.Turtle()
writer_3.penup()
writer_3.right(270)
writer_3.backward(50)
writer_3.right(90)
writer_3.pendown()

wn = trtl.Screen()
num_1 = float(wn.textinput("number","Pick a number: "))
side_1 = wn.textinput("side","Was that leg_1, leg_2, or hypotenuse? ")
num_2 = float(wn.textinput("number","Pick a number: "))
side_2 = wn.textinput("side","Was that leg_1, leg_2, or hypotenuse? ")

if side_1 == "leg_1":
    if side_2 == "leg_2":
        hypotenuse = (((num_1) ** 2) + ((num_2) ** 2)) ** 0.5
        area = (num_1 * num_2) / 2
        perimiter = num_1 + num_2 + hypotenuse
        writer_1.write("Hypotenuse: " + str(hypotenuse))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
elif side_1 == "leg_2":
    if side_2 == "leg_1":
        hypotenuse = (((num_1) ** 2) + ((num_2) ** 2)) ** 0.5
        area = (num_1 * num_2) / 2
        perimiter = num_1 + num_2 + hypotenuse
        writer_1.write("Hypotenuse: " + str(hypotenuse))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
elif side_1 == "hypotenuse":
    if side_2 == "leg_1":
        leg_2 = (((num_1) ** 2) - ((num_2) ** 2)) ** 0.5
        area = (num_2 * (leg_2)) / 2
        perimiter = num_2 + leg_2 + num_1
        writer_1.write("Leg_2: " + str(leg_2))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
elif side_1 == "leg_1":
    if side_2 == "hypotenuse":
        leg_2 = (((num_2) ** 2) - ((num_1) ** 2)) ** 0.5
        area = (num_1 * (leg_2)) / 2
        perimiter = num_1 + leg_2 + num_2
        writer_1.write("Leg_2: " + str(leg_2))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
elif  side_1 == "hypotenuse":
    if side_2 == "leg_2":
        leg_1 = (((num_1) ** 2) - ((num_2) ** 2)) ** 0.5
        area = (num_2 * (leg_1)) / 2
        perimiter = num_2 + leg_1 + num_1
        writer_1.write("Leg_1: " + str(leg_1))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
elif  side_1 == "leg_2":
    if side_2 == "hypotenuse":
        leg_1 = (((num_2) ** 2) - ((num_1) ** 2)) ** 0.5
        area = (num_1 * (leg_1)) / 2
        perimiter = num_1 + leg_1 + num_2
        writer_1.write("Leg_1: " + str(leg_1))
        writer_2.write("Area: " + str(area))
        writer_3.write("Perimiter: " + str(perimiter))
    else:
        writer_1.write("You are dumb. You did something wrong")
else:
    writer_1.write("You are dumb. You did something wrong")

wn.mainloop()