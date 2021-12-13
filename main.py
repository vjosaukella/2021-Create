# Import Stuff
import turtle as trtl

# Add Variables
maze = trtl.Turtle()
wn = trtl.Screen()
pacman = trtl.Turtle()
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


def travel():
    pacman.forward(speed)
    wn.ontimer(travel, 10)


wn.onkeypress(lambda: pacman.setheading(90), "Up")
wn.onkeypress(lambda: pacman.setheading(180), "Left")
wn.onkeypress(lambda: pacman.setheading(0), "Right")
wn.onkeypress(lambda: pacman.setheading(270), "Down")

#Make Pacman stop if encounters maze



wn.listen()
travel()

wn.mainloop()

# Points
# Scoreboard
