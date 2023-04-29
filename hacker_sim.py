#Importing necessary libraries
import turtle
import random

#Creating the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hacker Simulator")

#Creating the turtle
hacker = turtle.Turtle()
hacker.speed(0)
hacker.color("green")

#Function to create random characters
def create_char():
    char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+}{\":?><,./;'[]-=`\|")
    return char

#Function to draw the characters
def draw_char():
    hacker.penup()
    hacker.hideturtle()
    hacker.setpos(random.randint(-300, 300), random.randint(-300, 300))
    hacker.write(create_char(), font=("Courier", 16, "normal"))

#Loop to draw the characters continuously
while True:
    draw_char()

#Exiting the screen
turtle.done()
