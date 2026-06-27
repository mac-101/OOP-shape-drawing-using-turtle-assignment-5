import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

class Square:
    def __init__(self, pen, size):
        self.pen = pen
        self.size = size
        self.x = random.randint(-350, 350)
        self.y = random.randint(-350, 350)
        self.angle = random.randint(0, 360)
        self.color = (random.random(), random.random(), random.random())
    
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        self.pen.color(self.color)
        self.pen.pendown()
        
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.right(90)

while True:
    user_input = screen.textinput("Square Drawer", "How many squares? \nType 'q' to quit")
    
    if user_input is None or user_input.lower() == 'q':
        break  # exit the loop
    
    try:
        n = int(user_input)
        if n <= 0:
            continue  # skip if 0 or negative
        
        pen.clear()  # clear old squares before drawing new ones
        
        for _ in range(n):
            size = random.randint(20, 100)
            s = Square(pen, size)
            s.draw()
            
    except ValueError:
        # if user types "abc" instead of number
        screen.textinput("Error", "Please enter a valid number. Press OK to continue")

screen.bye()