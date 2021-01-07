# have the program ask for their q1 and q2 grades
# ask the user what they want their final grade to be
# then calculate the grade they need on the final and display as a letter

# 40% Q1 + 40% Q2 + 20% final = semester
# (semester - .4*Q1 - .4*Q2) / .2
# (90 - .4*97 - .4*86) / .2
# (90 - 38.8 - 34.4) / .2 = 84 >>> You need to get a B on the final to get an A in the class

# A = 90 - 100
# B = 80 - 89
# C = 70 - 79
# D = 60 - 69
# F = 0 - 59

import turtle as trtl
bob = trtl.Turtle()

# This block of code sets up the initial user inputs
q1 = input("What is your Quarter 1 percentage? (numbers only) ")
q1 = float(q1)
q2 = input("What is your Quarter 2 percentage? (numbers only) ")
q2 = float(q2)
semester = input("What percentage do you want for the semester? (numbers only) ")
semester = float(semester)

# Equation for the grade calculation... (semester - .4*Q1 - .4*Q2) / .2
final = (semester - (0.4 * q1) - (0.4 * q2)) / 0.2

print(final)

if final >= 90:
    print("A")
elif final >= 80 and final < 90:
    print("B")
elif final >= 70 and final < 80:
    print("C")
elif final >= 60 and final < 70:
    print("D")
else: 
    print("F")

#draws 0

def draw_0():
    bob.penup()
    bob.goto(-100,-100)
    bob.pendown()
    bob.right(90)
    bob.circle(50,180)
    bob.forward(100)
    bob.circle(50,180)
    bob.forward(100)

draw_0()

#draws 1

def draw_1():
    bob.penup()
    bob.goto(-100,-200)
    bob.pendown()
    bob.goto(-75,-175)
    bob.goto(-75,-275)
    bob.goto(-50,-275)
    bob.goto(-100,-275)
    
draw_1()

#draws 2

def draw_2():
    bob.penup()
    bob.goto(100,-100)
    bob.pendown()
    bob.right(180)
    bob.circle(-20,180)
    bob.goto(100,-150)
    bob.goto(140,-150)
    
draw_2()

#draws 3

def draw_3():
    bob.penup()
    bob.goto(100,0)
    bob.pendown()
    bob.right(180)
    bob.circle(-20,270)
    bob.right(180)
    bob.circle(-20,270)
    
draw_3()

#draws 4

def draw_4():
    bob.penup()
    bob.goto(100,200)
    bob.pendown()
    bob.goto(75,175)
    bob.goto(113,175)
    bob.penup()
    bob.goto(100,200)
    bob.pendown()
    bob.goto(100,150)

    
draw_4()

#draws 5

def draw_5():
    bob.penup()
    bob.goto(200,200)
    bob.pendown()
    bob.goto(160,200)
    bob.goto(160,160)
    bob.right(90)
    bob.circle(-40,180)
    
draw_5()

#draws 6

def draw_6():
    bob.penup()
    bob.goto(0,200)
    bob.pendown()
    bob.circle(50,180)
    bob.circle(25)
    
draw_6()

#draws 7

def draw_7():
    bob.penup()
    bob.goto(-100,200)
    bob.pendown()
    bob.goto(-50,200)
    bob.goto(-100,100)
    
draw_7()

#draws 8

def draw_8():
    bob.penup()
    bob.goto(-200,200)
    bob.pendown()
    bob.circle(-20)
    bob.right(180)
    bob.circle(-20,-360)

    
draw_8()

#draws 9

def draw_9():
    bob.penup()
    bob.goto(-200,100)
    bob.pendown()
    bob.circle(-20,630)
    bob.goto(-180,50)

    
draw_9()

window = trtl.Screen()
window.mainloop()


