''' Alex Vegso, 02/04/21, the code for the first one is supposed to draw a shape with the pen's shape and pen's color changing after every corner. The second one is supposed to write Fender in each color on the list using each shape with the corresponding color.'''
def turtles1():
  import turtle as trtl

  # makes a new empty list
  my_turtles = []

  # makes 2 new lists
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

  # it iterates through the shapes list, creates a new turtle with the shape from the list, and adds the turtle to the my_turtles list
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    my_turtles.append(t)
  
  # sets the starting x and the starting y equal to zero and the starting h to 90
  startx = 0
  starty = 0
  starth = 90
  # it starts a forloop for the pen to go up, to go to the start x and start y, make a setheading for the start h, make color on the list drawing on it, put the pen down, go right 45 degrees, anf forward 50
  for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(starth)
    col = turtle_colors.pop()
    t.color(col)
    t.pendown()
    t.right(45)     
    t.forward(50)

  #	it sets start x, y, and h to the current cordinates and current direction
    startx = t.xcor()
    starty = t.ycor()
    starth = t.heading()

  # it loops until the lists are done
  wn = trtl.Screen()
  wn.mainloop()


def turtles2():
  import turtle as trtl

  # makes a new empty list
  my_turtles = []

  # makes 2 new lists
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

  # it makes it so the shape is whatever is on the list
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    my_turtles.append(t)
  
  # sets the starting x equal to -300,  the starting y to -250
  startx = -300
  starty = -250
  starth = 90
  # it starts to write fender for every color and corresponding shape
  for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(starth)
    col = turtle_colors.pop()
    t.color(col)
    t.pendown()
    # writes the F
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    # writes the first e
    t.penup()
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(75)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.circle(25, 270)
    t.forward(25)
    # writes the n
    t.penup()
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.right(180)
    t.forward(25)
    t.right(180)
    t.circle(-25, 180)
    t.forward(25)
    # writes the d
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.pendown()
    t.circle(15)
    t.forward(50)
    # writes the second e
    t.penup()
    t.right(180)
    t.forward(65)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()
    t.forward(50)
    t.left(90)
    t.circle(25, 270)
    t.forward(25)
    # writes the r
    t.penup()
    t.forward(25)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.right(180)
    t.forward(25)
    t.right(180)
    t.circle(-25,110)

    #goes back to beginning and go to new cordinates to start the next color and the coresponding shape
    t.penup()
    t.goto(startx, starty)
    t.setheading(starth)
    t.pendown()
    t.forward(75)

  #	starts at the new cordinates
    startx = t.xcor()
    starty = t.ycor()
    starth = t.heading()

  # it loops until the lists are done
  wn = trtl.Screen()
  wn.mainloop()



def turtles3():
  import turtle as trtl
  import random

  # makes a new empty list
  my_turtles = []

  # makes 2 new lists
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

  # it makes it so the shape is whatever is on the list
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    my_turtles.append(t)
  
  # sets the starting x equal to -300,  the starting y to -250
  startx = random.randint(-200,200)
  starty = random.randint(-200,200)
  starth = random.randint(-200,200)
  # it starts to write fender for every color and corresponding shape
  for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(starth)
    col = turtle_colors.pop()
    t.color(col)
    t.pendown()
    # writes the F
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    # writes the first e
    t.penup()
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.pendown()
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.circle(random.randint(-50,50), random.randint(-180,180))
    t.forward(random.randint(-125,125))
    # writes the n
    t.penup()
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.pendown()
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.circle(random.randint(-50,50), random.randint(-180,180))
    t.forward(random.randint(-125,125))
    # writes the d
    t.penup()
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.pendown()
    t.circle(random.randint(-50,50), random.randint(-180,180))
    t.forward(random.randint(-125,125))
    # writes the second e
    t.penup()
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.pendown()
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.circle(random.randint(-50,50), random.randint(-180,180))
    t.forward(random.randint(-125,125))
    # writes the r
    t.penup()
    t.forward(random.randint(-125,125))
    t.left(random.randint(-180,180))
    t.pendown()
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.forward(random.randint(-125,125))
    t.right(random.randint(-180,180))
    t.circle(random.randint(-50,50),random.randint(-180,180))

    


  # it loops until the lists are done
  wn = trtl.Screen()
  wn.mainloop()


# asks user which function they want to use
function_chooser = int(input("Which function do you want to use? (1 or 2 or 3) "))
if (function_chooser == 1):
  turtles1()
elif (function_chooser == 2):
  turtles2()
elif (function_chooser == 3):
      turtles3()
else: 
  print("Function not defined")