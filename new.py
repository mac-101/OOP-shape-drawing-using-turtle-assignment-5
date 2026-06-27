import turtle
import random

def draw_random_squares(n):
    screen = turtle.Screen()
    screen.bgcolor("black")  # dark bg makes colors pop
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(0)  # fastest
    t.hideturtle()
    
    for _ in range(n):
        # Random properties
        size = random.randint(20, 100)
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        angle = random.randint(0, 360)
        
        # Random color
        r = random.random()
        g = random.random() 
        b = random.random()
        t.color(r, g, b)
        
        # Move + draw
        t.penup()
        t.goto(x, y)
        t.setheading(angle)
        t.pendown()
        
        for _ in range(4):
            t.forward(size)
            t.left(90)
    
    screen.exitonclick()

# Change this number to how many squares you want
num_squares = 30
draw_random_squares(num_squares)