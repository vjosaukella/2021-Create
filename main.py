# Import Stuff
import turtle as trtl
# Add Variables
t = trtl.Turtle()
wn = trtl.Screen()
pacman = trtl.Turtle()
#SetUp
pacman_image = "pacman.gif"
wn.addshape(pacman_image)
wn.title("PACMAN")
wn.setup(1000,900)
# set the turtle to the correct position
t.penup()
t.goto(-250, -200)
t.pensize(15)
t.speed("fastest")
t.pencolor("blue")
wn.bgcolor("black")
# making the maze
t.pendown()
t.forward(500)
t.left(90)
t.forward(500)
t.left(90)
t.forward(100)
t.penup()
t.forward(100)
t.pendown()
t.forward(300)
t.left(90)
t.forward(300)
t.penup()
t.forward(100)
t.pendown()
t.forward(100)
t.left(180)
t.penup()
t.forward(400)
# Making the inside of the maze
# FirstPart
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.penup()
t.forward(100)
# SecondPart
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
# ThirdPart
t.left(90)
t.forward(200)
# FourthPart
t.right(180)
t.forward(100)
t.left(90)
t.penup()
t.forward(100)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
# FifthPart
t.right(180)
t.forward(100)
t.right(90)
t.forward(100)
# SixthPart
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
# SeventhPart
t.left(180)
t.penup()
t.forward(200)
t.right(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
# EighthPart
t.left(180)
t.forward(100)
t.left(90)
t.penup()
t.forward(100)
t.pendown()
t.forward(100)
t.hideturtle()
# Create Pacman
pacman.penup()
pacman.shape(pacman_image)
#Make Pacman move
pacman.goto(-300,-50)
pacman.speed(0)







# Points
# Scoreboard


wn.mainloop()
