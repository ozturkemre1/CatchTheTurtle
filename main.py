import turtle
import random

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("pink")
drawing_screen.title("Catch the Turtle")
FONT = ("Arial",30,"normal")
score = 0
gameOver = False

#turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()
#countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = drawing_screen.window_height()/2
    y = top_height * 0.85
    score_turtle.setpos(0-100,y)
    score_turtle.write(arg="Score: 0",move=False,align="center",font=FONT)

grid_size = 15
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

        #print(x ,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("midnight blue")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)



x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10,-20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not gameOver:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global gameOver
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = drawing_screen.window_height() / 2
    y = top_height * 0.85
    countdown_turtle.setpos(100, y)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        drawing_screen.ontimer(lambda: countdown(time-1),1000)
    else:
        gameOver = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)

turtle.mainloop()