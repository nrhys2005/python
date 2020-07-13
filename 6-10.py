import turtle

t = turtle.Turtle()
t.shape("turtle")

count = 0

while True:
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.left(90)
    count+=1
    #if count ==10:
     #   break;

