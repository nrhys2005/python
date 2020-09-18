import turtle
def drawSnowman(x,y,ratio,name):
    #left_arm
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(115)
    t.forward(100*ratio)

    #right_arm
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(65)
    t.forward(100*ratio)

    t.setheading(0)

    #head
    t.up()
    t.goto(x, y+(80*ratio))
    t.down()
    t.begin_fill()
    t.circle(30*ratio)
    t.end_fill()

    #neck
    t.up()
    t.goto(x, y+(60*ratio))
    t.down()
    t.begin_fill()
    t.circle(15*ratio)
    t.end_fill()
    
    #body
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.circle(40*ratio)
    t.end_fill()

    t.up()
    t.goto(x-(len(name)*5), y+(40*ratio)-5)
    t.down()
    t.write(name)

t = turtle.Turtle()
t.shape("turtle")

s = turtle.Screen()
s.bgcolor('skyblue')
t.fillcolor('white')
drawSnowman(-150, 0, 1.2, "엄마눈사람")
drawSnowman(0, 0, 1.0, "이상훈") 
drawSnowman(150, 0, 1.3, "아빠눈사람")


