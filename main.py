# Import Stuff
import turtle as trtl
import time

# Initiaze Turtles
maze = trtl.Turtle()
wn = trtl.Screen()
pacman = trtl.Turtle()

counter = trtl.Turtle()
counter.penup()
counter.pencolor("white")
counter.goto(-300, 400)
counterInterval = 1000
timer = 45
timerUp = False
fontSetup = ("Arial", 21, "white")
# SetUp
pacman_image = "pacman.gif"
wn.addshape(pacman_image)
wn.title("PACMAN")
wn.setup(1000, 900)
# set the turtle to the correct position
maze.penup()
maze.goto(-250, -200)
maze.pensize(15)
maze.speed("fastest")
maze.pencolor("blue")
wn.bgcolor("black")
# making the maze
maze.pendown()
maze.forward(500)
maze.left(90)
maze.forward(500)
maze.left(90)
maze.forward(100)
maze.penup()
maze.forward(100)
maze.pendown()
maze.forward(300)
maze.left(90)
maze.forward(300)
maze.penup()
maze.forward(100)
maze.pendown()
maze.forward(100)
maze.left(180)
maze.penup()
maze.forward(400)
# Making the inside of the maze
# FirstPart
maze.pendown()
maze.right(90)
maze.forward(100)
maze.right(90)
maze.forward(200)
maze.penup()
maze.forward(100)
# SecondPart
maze.left(90)
maze.pendown()
maze.forward(100)
maze.right(90)
maze.forward(100)
maze.left(90)
maze.forward(100)
# ThirdPart
maze.left(90)
maze.forward(200)
# FourthPart
maze.right(180)
maze.forward(100)
maze.left(90)
maze.penup()
maze.forward(100)
maze.left(90)
maze.pendown()
maze.forward(100)
maze.right(90)
maze.forward(100)
# FifthPart
maze.right(180)
maze.forward(100)
maze.right(90)
maze.forward(100)
# SixthPart
maze.left(90)
maze.forward(200)
maze.left(90)
maze.forward(100)
# SeventhPart
maze.left(180)
maze.penup()
maze.forward(200)
maze.right(90)
maze.pendown()
maze.forward(100)
maze.left(90)
maze.forward(100)
# EighthPart
maze.left(180)
maze.forward(100)
maze.left(90)
maze.penup()
maze.forward(100)
maze.pendown()
maze.forward(100)
maze.hideturtle()
# Create Pacman
pacman.penup()
pacman.shape(pacman_image)
# Make Pacman move
pacman.goto(-300, -50)
pacman.speed(0)
speed = 1.5


def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        counter.write("Time is up!", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)


def travel():
    pacman.forward(speed)
    wn.ontimer(travel, 10)


wn.onkeypress(lambda: pacman.setheading(90), "Up")
wn.onkeypress(lambda: pacman.setheading(180), "Left")
wn.onkeypress(lambda: pacman.setheading(0), "Right")
wn.onkeypress(lambda: pacman.setheading(270), "Down")

wn.listen()
travel()
# Make Pacman stop if encounters border
while True:
    pacman.forward(speed)

    if pacman.xcor() > 400 or pacman.xcor() < -400:
        pacman.right(180)
    if pacman.ycor() > 400 or pacman.ycor() < -300:
        pacman.right(180)

# Points
# Scoreboard
