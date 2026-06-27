import turtle

screen = turtle.Screen()
pen = turtle.Turtle()


class Shape:
    def __init__(self, size, color, pen):
        self.size = size
        self.color = color
        self.pen = pen


class Circle(Shape):
    def draw(self):
        self.pen.color(self.color)
        self.pen.circle(self.size)


class Square(Shape):
    def draw(self):
        self.pen.color(self.color)
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.right(90)


class Octagon(Shape):
    def draw(self):
        self.pen.color(self.color)
        for _ in range(8):
            self.pen.forward(self.size)
            self.pen.right(45)

def verify_choice(choice):
    return choice in ["circle", "square", "octagon"]


# ===== input =====

while True:
    choice = input("circle / square / octagon (or exit): ").lower()

    if choice == "exit":
        print("Goodbye")
        break
    
    if not verify_choice(choice):
        print("Pick a valid shape")
        continue
            
    size = int(input("size: "))
    color = input("color: ")

    shape = None

    if choice == "circle":
        shape = Circle(size, color, pen)
    elif choice == "square":
        shape = Square(size, color, pen)
    elif choice == "octagon":
        shape = Octagon(size, color, pen)

    shape.draw()

turtle.done()