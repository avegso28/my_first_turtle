''' Alex Vegso 
    this program uses turtle module to draw a tower with different colored floors based on the number of the floor. Ex. all even floors blue, all odd floors grey
'''
# set the turtle
# set tower width
# set tower height
# set floor counter
# while floor number is less than tower height
#   if the floor number is an even multiple of 5
#       set color to green
#   else
#       set the color to red
# move the painter forward tower width
# increase the floor number 
# move the painter backwards the tower width

import turtle as trtl

rem = 0
switcher = 10
floor_height = 5
tower_width = 50
x = -150
y = -150

bob = trtl.Turtle()
bob.speed(0)
bob.pensize(floor_height)

height = 60
floor = 0

while floor < height:
    bob.penup()
    bob.goto(x,y)
    rem = floor % switcher
    if rem >= (switcher / 2):
        bob.color("red")
    else:
        bob.color("green")
    y += floor_height
    floor += 1
    bob.pendown()
    bob.forward(tower_width)

window = trtl.Screen()
window.mainloop()

