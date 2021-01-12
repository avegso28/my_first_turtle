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




ones = final%10
tens = (final-ones)/10

if tens == 0:
    print("tens is zero")
elif tens == 1:
    print("tens is one")
elif tens == 2:
    print("tens is two")
elif tens == 3:
    print("tens is three")
elif tens == 4:
    print("tens is four")
elif tens == 5:
    print("tens is five")
elif tens == 6:
    print("tens is six")
elif tens == 7:
    print("tens is seven")
elif tens == 8:
    print("tens is eight")
elif tens == 9:
    print("tens is nine")

if ones == 0:
    print("ones is zero")
elif ones == 1:
    print("ones is one")
elif ones == 2:
    print("ones is two")
elif ones == 3:
    print("ones is three")
elif ones == 4:
    print("ones is four")
elif ones == 5:
    print("ones is five")
elif ones == 6:
    print("ones is six")
elif ones == 7:
    print("ones is seven")
elif ones == 8:
    print("ones is eight")
elif ones == 9:
    print("ones is nine") 

round = float(final) - int(final)

if round >= .5:
    rounded_ones = ones + 1
if round < .5:
    rounded_ones = ones

print(int(tens))
print(int(rounded_ones))

#draws 0

def draw_0():
    bob.penup()
    bob.pendown()
    bob.right(90)
    bob.circle(25,180)
    bob.forward(50)
    bob.circle(25,180)
    bob.forward(50)
def ones_0():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_0()
def tens_0():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_0()
if ones == 0:
    ones_0() 
if tens == 0:
    tens_0()

#draws 1

def draw_1():
    bob.penup()
    bob.pendown()
    bob.left(135)
    bob.forward(25)
    bob.right(135)
    bob.forward(75)
    bob.right(90)
    bob.forward(25)
    bob.right(180)
    bob.forward(50)
    
def ones_1():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_1()
def tens_1():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_1()
if ones == 1:
    ones_1() 
if tens == 1:
    tens_1()

#draws 2

def draw_2():
    bob.penup()
    bob.pendown()
    bob.right(270)
    bob.circle(-25,180)
    bob.right(35)
    bob.forward(70)
    bob.left(125)
    bob.forward(50)
    
def ones_2():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_2()
def tens_2():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_2()
if ones == 2:
    ones_2() 
if tens == 2:
    tens_2()

#draws 3

def draw_3():
    bob.penup()
    bob.pendown()
    bob.right(270)
    bob.circle(-20,270)
    bob.right(180)
    bob.circle(-20,270)
    
def ones_3():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_3()
def tens_3():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_3()
if ones == 3:
    ones_3() 
if tens == 3:
    tens_3()

#draws 4

def draw_4():
    bob.penup()
    bob.pendown()
    bob.right(45)
    bob.forward(50)
    bob.right(135)
    bob.forward(100)
    bob.penup()
    bob.backward(100)
    bob.left(135)
    bob.backward(50)
    bob.pendown()
    bob.right(45)
    bob.forward(50)
    
def ones_4():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_4()
def tens_4():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_4()
if ones == 4:
    ones_4() 
if tens == 4:
    tens_4()

#draws 5

def draw_5():
    bob.penup()
    bob.pendown()
    bob.right(180)
    bob.forward(40)
    bob.left(90)
    bob.forward(40)
    bob.right(45)
    bob.circle(20,-225)
    
def ones_5():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_5()
def tens_5():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_5()
if ones == 5:
    ones_5() 
if tens == 5:
    tens_5()

#draws 6

def draw_6():
    bob.penup()
    bob.pendown()
    bob.circle(50,180)
    bob.circle(25)
    
def ones_6():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_6()
def tens_6():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_6()
if ones == 6:
    ones_6() 
if tens == 6:
    tens_6()

#draws 7

def draw_7():
    bob.penup()
    bob.pendown()
    bob.forward(50)
    bob.right(112.5)
    bob.forward(75)

    
def ones_7():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_7()
def tens_7():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_7()
if ones == 7:
    ones_7() 
if tens == 7:
    tens_7()

#draws 8

def draw_8():
    bob.penup()
    bob.pendown()
    bob.left(112.5)
    bob.circle(-20)
    bob.right(180)
    bob.circle(-20,-360)

    
def ones_8():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_8()
def tens_8():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_8()
if ones == 8:
    ones_8() 
if tens == 8:
    tens_8()

#draws 9

def draw_9():
    bob.penup()
    bob.pendown()
    bob.right(90)
    bob.circle(-20,630)
    bob.forward(75)



def ones_9():
    bob.penup()
    bob.goto(0,0)
    bob.pendown()
    draw_9()
def tens_9():
    bob.penup()
    bob.goto(-100,0)
    bob.pendown()
    draw_9()
if ones == 9:
    ones_9() 
if tens == 9:
    tens_9()   

window = trtl.Screen()
window.mainloop()


