import turtle
import random

def snowman(x,y):
    t.fillcolor("white")
    t.up()
    t.goto(x,y)
    
    t.down()
    t.begin_fill()
    t.circle(40)#위 원
    t.end_fill()

    t.up()#이동
    t.right(90)
    t.forward(50)
    t.left(90)
    
    t.down()
    t.left(20)  #팔그리기
    t.forward(100)
    t.backward(100)
    t.left(120)
    t.forward(100)
    t.backward(100)
    t.right(140)
    

    t.begin_fill()
    t.circle(30)#중간 원
    t.end_fill()
    
    t.up()#이동
    t.right(90)
    t.forward(90)
    t.left(90)

    t.down()
    t.begin_fill()
    t.circle(60)#아래 원
    t.end_fill() 
    
t = turtle.Turtle()
s=turtle.Screen()
s.bgcolor("skyblue")

for i in range(3):
    x=random.randint(1,400)
    y=random.randint(-100,100)
    snowman(x,y)

