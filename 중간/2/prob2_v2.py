import turtle

def drawFlower():
    for _ in range(36):
        i=0
        while i<5:
            t.forward(100)
            t.right(144)
            i=i+1
        t.left(10)

t = turtle.Turtle()
t.shape("turtle")
t.right(180)
t.color('red')
drawFlower()
