''' Alex Vegso, 2/17/21
Create a turtle in a random location. If turtle is clicked have the turtle move to a new random location add 1 point to score.'''


#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
shape = "turtle"
color = "Green"
speed = 0
score = 1
size_list = []
font_setup = ("Arial", 20, "normal")
time_keeper = 30
timer_interval = 1000
time_up = False 


#-----initialize turtle-----
jumpy = trtl.Turtle()
jumpy.shape(shape)
jumpy.shapesize(3)
jumpy.color(color)
jumpy.penup()
jumpy.speed(speed)

writer = trtl.Turtle()
writer.speed(speed)
writer.hideturtle()
writer.penup()
writer.goto(0,290)

timer = trtl.Turtle()
timer.speed(speed)
timer.hideturtle()
timer.penup()
timer.goto(0, 260)

wn = trtl.Screen()


#-----game functions-------
def list_maker():
    global size_list
    num = 0.1
    size_list = []
    for i in range (30):
        size_list.append(num)
        num += 0.1
        i += 1

def start_message():
    start = "Click turtle to start"
    writer.write(start, font=font_setup)
    start_time = "time"
    timer.write(start_time, font=font_setup)


def game(x, y):
    jumpy.onclick(jumpy_clicked)
    wn.onclick(jumpy_not_clicked)
    wn.ontimer(timer_countdown, timer_interval)


def jumpy_clicked(x, y):
    global time_up
    global size_list
    if (not time_up):
        size = size_list.pop()
        jumpy.shapesize(size)
        increase_score()
        change_pos()
    else: 
        jumpy.hideturtle()


def change_pos():
    new_x = rand.randint(-250, 250)
    new_y = rand.randint(-250, 250)
    jumpy.goto(new_x, new_y)


def increase_score():
    global score
    score += 2
    writer.clear()
    writer.write(score, font=font_setup)


def jumpy_not_clicked(x, y):
    global time_up
    if (not time_up):
        decrease_score()

    else: 
        jumpy.hideturtle()


def decrease_score():
    global score
    score -= 1
    writer.clear()
    writer.write(score, font=font_setup)




def timer_countdown():
    global time_keeper, time_up
    timer.clear()
    if time_keeper <= 0:
        time_up = True
    else:
        timer.write(("Time: " + str(time_keeper)), font=font_setup)
        time_keeper -= 1
        timer.getscreen().ontimer(timer_countdown, timer_interval)


#-----events----------------
list_maker()
start_message()
jumpy.onclick(game)
wn.mainloop()
