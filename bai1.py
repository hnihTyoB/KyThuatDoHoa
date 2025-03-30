import turtle
from turtle import *

def drawOxy():
    #Vẽ lưới
    pencolor('#C0C0C0')
    penup()
    goto(-330, 330)
    pensize(0.5)
    for i in range(330, -335, -5):
        goto(-330, i)   
        pendown()
        forward(660)
        penup()
    right(90)
    goto(-330, 330)
    for i in range(-330, 335, 5):
        goto(i, 330)   
        pendown()
        forward(660)
        penup()   
    left(90)

    pencolor('black')
    pensize(2)
    #Vẽ trục Ox
    penup()
    goto(-250, 0)
    pendown()
    forward(500)
    write('x', align='left', font=('arial', 15, 'normal'))
    #Vẽ trục Oy
    penup()
    goto(0, -250)
    pendown()
    left(90)    
    forward(500)
    write('y', align='left', font=('arial', 15, 'normal'))
    #Vẽ điểm O
    penup()
    goto(-10, -30)
    pendown()
    write('O', align='right', font=('arial', 15, 'normal'))
    #Vẽ các đường kẻ ngang
    penup()
    pensize(1)
    for i in range(-245, 250, 5):
        goto(i, -5)
        pendown()
        forward(11)
        penup()
    #Vẽ các đường kẻ dọc
    right(90)
    for i in range(-245, 250, 5):
        goto(-5, i)
        pendown()
        forward(10)
        penup()

def drawPoint(x, y):
    penup()
    goto(x, y)
    pendown()
    dot(5, 'red')
    penup()
    goto(x, y + 10)
    write(f'({x}, {y})', align='center', font=('arial', 10, 'normal'))

def main():
    turtle.tracer(0)
    turtle.setup(700, 700)
    drawOxy()
    onscreenclick(drawPoint)
    turtle.done()

if __name__ == "__main__":
    main()