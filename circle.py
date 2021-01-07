import turtle as trtl

# circle
def draw_circle():
    side = input("How long do you want your sides? ")
    side = float(side)
    i = 0
    bob = trtl.Turtle()

    while i < 360:
        bob.forward(1)
        bob.right(1)
        i += 1

# square
def draw_square():
    side = input("How long do you want your sides? ")
    side = float(side)
    i = 0
    bob = trtl.Turtle()

    while i < 4:
        bob.forward(side)
        bob.right(90)
    i += 1

# octogon
def draw_octogon():
    side = input("How long do you want your sides? ")
    side = float(side)
    i = 0
    bob = trtl.Turtle()

    while i < 8:
        bob.forward(side)
        bob.right(45)
        i += 1

draw_octogon()

window = trtl.Screen()
window.mainloop()