from turtle import *
import time
from random import randint
speed(10)
penup()
goto(-140,140)

for step in range(6):
    write(step,align='center')
    right(90)
    forward(15)
    pendown()
    forward(150)
    penup()
    backward(165)
    left(90)
    time.sleep(0.5)
    forward(33)

ada=Turtle()
ada.color('orange')
ada.shape('turtle')

bob=Turtle()
bob.color('violet')
bob.shape('turtle')

tim=Turtle()
tim.color('green')
tim.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

bob.penup()
bob.goto(-160,70)
bob.pendown()

tim.penup()
tim.goto(-160,40)
tim.pendown()


for turn  in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    tim.forward(randint(1,5))


