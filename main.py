import turtle as trtl

painter = trtl.Turtle()

painter.pencolor('green')
painter.penup()
painter.goto(-60,0)
painter.right(90)
painter.forward(100)
painter.pendown()
painter.left(180)
painter.forward(250)
painter.right(90)
painter.forward(80)
painter.right(90)
painter.forward(250)
painter.right(90)
painter.forward(80)
painter.pencolor('orange')
painter.goto(-60,-125)
painter.goto(-50,-100)
painter.goto(-40,-125)
painter.goto(-30,-100)
painter.goto(-20,-125)
painter.goto(-10,-100)
painter.goto(-0,-125)
painter.goto(10,-100)
painter.goto(20,-125)
painter.goto(20,-100)
painter.penup()
painter.goto(-60,150)
painter.pendown()
painter.pencolor('blue')
painter.goto(-20,200)
painter.goto(20,150)
painter.penup()
painter.goto(20,-100)
painter.pendown()
painter.pencolor('red')
painter.right(180)
painter.forward(80)
painter.goto(20,-50)
painter.penup()
painter.goto(-60,-100)
painter.pendown()
painter.right(180)
painter.forward(80)
painter.goto(-60,-50)
painter.penup()
painter.goto(-20,100)
painter.pendown()
painter.pencolor('purple')
painter.circle(20)

window = trtl.Screen()
window.mainloop()
