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
size_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]
size_list_copy = []
font_setup = ("Arial", 20, "normal")
time_keeper = 30
timer_interval = 1000
time_up = False 
size_list_copy = size_list

#-----initialize turtle-----
jumpy = trtl.Turtle()
jumpy.shape(shape)
jumpy.shapesize(size_list.pop())
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


#-----game functions--------
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
        size = size_list_copy.pop()
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
start_message()
jumpy.onclick(game)
wn.mainloop()
