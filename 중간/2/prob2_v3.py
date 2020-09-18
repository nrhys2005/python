import turtle

def drawFlower(radius, size, color):
    t.color(color)
    max_radius=0
    while True:
        i=0
        while i<5:
            t.forward(size)
            t.right(144)
            i=i+1
        t.left(radius)
        max_radius+=radius
        if(max_radius>=360):
            break;

t = turtle.Turtle()
t.shape("turtle")
t.right(180)
t.color('red')
drawFlower(10, 150, 'blue')
drawFlower(15, 100, 'red')
drawFlower(30, 50, 'yellow')
