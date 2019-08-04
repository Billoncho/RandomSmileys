# RandomSmilies.py
# Billy Ridgeway
# Generates randomly placed smiley faces.

import random               # Imports the random library.
import turtle               # Imports the turtle library.
t = turtle.Pen()            # Creates a new turtle pen called t.
t.speed(0)                  # Sets the pen's speed to fast.
t.hideturtle()              # Hides the pen.
turtle.bgcolor("black")     # Sets the background to black.

# Creates a smiley face.
def draw_smiley(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

    # Head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Left eye
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Right eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

# Creates a for loop and draws the smiley in random x and y locations
# 50 times.
for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    draw_smiley(x,y)
    
