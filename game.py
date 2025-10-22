import turtle
import random
import time
from pixels import check_pixel_color

# Constants
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 800
WINDOW_TITLE = "My First Turtle Program"

CADETBLUE_POINTS = 50
NAVY_POINTS = 20

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle object
t = turtle.Turtle()
flash = turtle.Turtle()
rocket = turtle.Turtle()
rocket.color("Red", "White")
rocket.shape("triangle")

screen.tracer(0)
screen.bgcolor("Black")
t.pencolor("White")
t.hideturtle()
flash.hideturtle()
rocket.hideturtle()

total_score = 0

## Drawing star background
for star_num in range(500):
    x = random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2)
    y = random.randint(-SCREEN_HEIGHT//3, SCREEN_HEIGHT//2)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fd(6)
    t.bk(3)
    t.left(90)
    t.fd(3)
    t.bk(6)
    t.penup()

## Center asteroid
size = random.randint(15,45)
angle = random.randint(-360,360)
color_choice = random.randint(0, 1)
color = "CadetBlue" * (color_choice == 0) + "Navy" * (color_choice == 1)

t.fillcolor(color)
t.goto(0,0)
t.setheading(angle)

t.begin_fill()
for i in range(6):
    t.pendown()
    t.forward(size)
    t.left(60)
t.end_fill()
t.penup()

## Asteroids
for asteroid_num in range(15):
    asteroid_x = random.randint(-SCREEN_WIDTH//2, SCREEN_WIDTH//2)
    asteroid_y = random.randint(-SCREEN_HEIGHT//3, SCREEN_HEIGHT//2)
    size = random.randint(15,45)
    angle = random.randint(-360,360)
    color_choice = random.randint(0, 1)
    color = "CadetBlue" * (color_choice == 0) + "Navy" * (color_choice == 1)

    t.fillcolor(color)
    t.penup()
    t.goto(asteroid_x,asteroid_y)
    t.setheading(angle)

    t.begin_fill()
    for y in range(6):
        t.pendown()
        t.forward(size)
        t.left(60)
    t.end_fill()

screen.update()
time.sleep(1.2)

## Get # of shots from player
num_shots = screen.numinput("Play time!","How many shots would  you like?", minval=1, maxval=100, default = 3)

## Main game loop
for i in range(int(num_shots)):
    points_earned = 0
    asteroid_hit = 0
    pos_x = screen.numinput(f"shot number {i+1}", "Enter x coordinate: ")
    pos_y = screen.numinput(f"shot number {i+1}", "Enter y coordinate: ")

    points_earned += check_pixel_color(pos_x,pos_y, "CadetBlue")* CADETBLUE_POINTS + check_pixel_color(pos_x, pos_y, "Navy")* NAVY_POINTS

    rocket.penup()
    rocket.goto(-SCREEN_WIDTH//2 + 20, -SCREEN_HEIGHT//2 + 20)
    rocket.showturtle()
    rocket.seth(rocket.towards(pos_x, pos_y))

## Calculate distance and animation steps using equation of line(rocket animation)

    deltax = pos_x - rocket.xcor()
    deltay = pos_y - rocket.ycor()
    distance = (deltax**2 + deltay**2)**0.5
    animation_steps = int((distance/20))

    for step in range (animation_steps + 1):
        rocket.setheading(rocket.towards(pos_x, pos_y))
        rocket.forward(20)
        screen.update()
        time.sleep(0.015)

    for y in range (-20, 20):
        for x in range(-20, 20):
            points_earned += check_pixel_color(pos_x+x,pos_y+y, "CadetBlue")* CADETBLUE_POINTS * (asteroid_hit == 0) # This is          saying that if the pixel color matches, add it to the points variable only if we haven't found anything yet i.e asteroid_hit == 0
            points_earned += check_pixel_color(pos_x+x, pos_y+y, "Navy")* NAVY_POINTS * (asteroid_hit == 0)

            asteroid_hit += (points_earned > 0) * (asteroid_hit == 0) # Here we're using a boolean to update found to 1, so more points are not added later on.

    rocket.hideturtle()
    total_score += points_earned

## Flash effect

    flash.penup()
    flash.goto(pos_x, pos_y - 20)
    flash.pendown()
    flash.fillcolor("Red")
    flash.begin_fill()
    flash.circle(20)
    flash.end_fill()
    flash.penup()

## Display points earned

    flash.goto(pos_x, pos_y - 10)
    flash.pendown()
    flash.write(f"+{points_earned}", align = 'center', font=('Comic Sans MS', 14, 'bold'))
    flash.penup()
    screen.update()
    time.sleep(0.5)

t.penup()
t.goto(0,-350)
t.write(f"Total score: {total_score}", font=('Comic Sans MS', 18), align = 'center')
## End of your code

# Make a clean exit
screen.exitonclick()
