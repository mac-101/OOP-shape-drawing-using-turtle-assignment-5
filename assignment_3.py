import turtle
import random

screen = turtle.Screen()
screen.setup(width=900, height=700)

bg_color = (random.random(), random.random(), random.random())
screen.bgcolor(bg_color)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()  # hide the arrow too

class Shape:
    def __init__(self, pen, sides):
        self.pen = pen
        self.sides = sides
        self.size = random.randint(60, 120)
        self.x = random.randint(-400, 400)
        self.y = random.randint(-300, 300)
        self.angle = random.randint(0, 360)
        self.color = (random.random(), random.random(), random.random())
    
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        
        # 1. Set both outline + fill color to the object's color
        self.pen.color(self.color)      
        self.pen.fillcolor(self.color)  
        
        self.pen.pendown()
        self.pen.begin_fill()  # <-- start filling
        
        angle = 360 / self.sides
        for _ in range(self.sides):
            self.pen.forward(self.size)
            self.pen.right(angle)
        
        self.pen.end_fill()  # <-- stop filling

class Rectangle(Shape):
    def __init__(self, pen):
        super().__init__(pen, 4)
        self.width = random.randint(60, 150)
        self.height = random.randint(40, 100)
    
    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        
        self.pen.color(self.color)
        self.pen.fillcolor(self.color)
        
        self.pen.pendown()
        self.pen.begin_fill()
        
        for _ in range(2):
            self.pen.forward(self.width)
            self.pen.right(90)
            self.pen.forward(self.height)
            self.pen.right(90)
        
        self.pen.end_fill()

shapes = [
    Shape(pen, 4),
    Rectangle(pen),  
    Shape(pen, 3),
    Shape(pen, 6),
    Shape(pen, 8)
]

random.shuffle(shapes)

for shape in shapes:
    shape.draw()

screen.exitonclick()