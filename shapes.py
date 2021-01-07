import turtle as trtl


def draw_triangle():  # defines the equalateral triangle function
    i = 0  # sets the counter equal to 0
    while i <= 2:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(120)  # angle = 360 / number of sides
        i += 1  # adds 1 to the counter


def draw_square():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 2:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(90)  # angle = 360 / number of sides
        i += 1  # adds 1 to the counter


# hexagon
def draw_hexagon(): # defines the hexagon function
    i = 0 # sets the counter equal to 0
    while i <= 5: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/6) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter
# heptagon
def draw_heptagon(): # defines the heptagon function
    i = 0 # sets the counter equal to 0
    while i <= 6: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/7) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter
# octogon
def draw_octagon(): # defines the octagon function
    i = 0 # sets the counter equal to 0
    while i <= 7: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/8) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter
# nonagon
def draw_nonagon(): # defines the nonagon function
    i = 0 # sets the counter equal to 0
    while i <= 8: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/9) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter
# decagon
def draw_decagon(): # defines the decagon function
    i = 0 # sets the counter equal to 0
    while i <= 9: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/10) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter
# circle
def draw_circle(): # defines the circle function
    i = 0 # sets the counter equal to 0
    while i <= 359: # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side) # moves forward the user input amount
        fred.right(360/360) # angle = 360 / number of sides
        i += 1 # adds 1 to the counter


fred = trtl.Turtle()  # defines the name of my turtle as fred
fred.shape("turtle")  # changes the painter shape from an arrow to a turtle...becasue I can...
window = trtl.Screen()

again = "Y"
while again.upper() == "Y":
    shape = trtl.textinput("Number of Sides:", "How many sides do you want to draw?")
    side = trtl.textinput("Side Length:", "How long do you want your sides?")
    side = float(side)

    if shape == "3":
        draw_triangle() #if 3, draws a triangle
    elif shape == "4":
        draw_square() #if 4, draws a square
    elif shape == "6":
        draw_hexagon() #if 6, draws a hexagon
    elif shape == "7":
        draw_heptagon() #if 7, draws a heptagon
    elif shape == "8":
        draw_octagon() #if 8, draws a octagon
    elif shape == "9":
        draw_nonagon() #if 9, draws a nonagon
    elif shape == "10":
        draw_decagon() #if 10, draws a decagon
    elif shape == "0":
        draw_circle() #if 0, draws a circle
    else:
        print("not in my programing...")

    again = trtl.textinput("New Shape:", "Draw a new shape?(Y/N")
    fred.clear() #clears the screen of all drawings

window.done()
