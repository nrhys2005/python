import turtle
def drawSnowman(x,y):
    #left_arm
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(115)
    t.forward(100)

    #right_arm
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(65)
    t.forward(100)

    t.setheading(0)

    #head
    t.up()
    t.goto(x, y+80)
    t.down()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    #neck
    t.up()
    t.goto(x, y+60)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    #body
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.up()
    t.goto(x-15, y+30)
    t.down()
    t.write("눈사람")

t = turtle.Turtle()
t.shape("turtle")

s = turtle.Screen()
s.bgcolor('skyblue')
t.fillcolor('white')
drawSnowman(-150, 0)
drawSnowman(0, 0)
drawSnowman(150, 0)


