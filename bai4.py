import turtle
from tkinter import *

def drawOxy():
    #Vẽ lưới
    p.pencolor('#C0C0C0')
    p.penup()
    p.goto(-330, 330)
    p.pensize(0.5)
    for i in range(330, -335, -5):
        p.goto(-330, i)   
        p.pendown()
        p.forward(660)
        p.penup()
    p.right(90)
    p.goto(-330, 330)
    for i in range(-330, 335, 5):
        p.goto(i, 330)   
        p.pendown()
        p.forward(660)
        p.penup()   
    p.left(90)

    p.pencolor('black')
    p.pensize(2)
    #Vẽ trục Ox
    p.penup()
    p.goto(-300, 0)
    p.pendown()
    p.forward(600)
    p.write('x', align='left', font=('arial', 15, 'normal'))
    #Vẽ trục Oy
    p.penup()
    p.goto(0, -300)
    p.pendown()
    p.left(90)    
    p.forward(600)
    p.write('y', align='left', font=('arial', 15, 'normal'))
    #Vẽ điểm O
    p.penup()
    p.goto(-2, -22)
    p.pendown()
    p.write('O', align='right', font=('arial', 15, 'normal'))
    #Vẽ các đường kẻ ngang
    p.penup()
    p.pensize(1)
    for i in range(-275, 300, 25):
        p.goto(i, -5)
        p.pendown()
        p.forward(11)
        p.penup()
        if i != 0:
            p.write(i//5, align='center', font=('arial', 10, 'normal'))
    #Vẽ các đường kẻ dọc
    p.right(90)
    for i in range(-275, 300, 25):
        p.goto(-5, i)
        p.pendown()
        p.forward(10)
        p.penup()
        if i != 0:
            p.goto(-15, i-8)
            p.write(i//5, align='center', font=('arial', 10, 'normal'))

def drawPoint(x, y):
    x *= 5
    y *= 5
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5, 'red')

def drawHinhEllipse(x, y, a, b):
    t.clear()
    x_i, y_i = 0, b
    P = b**2 - a**2 * b + a**2 / 4
    len_dash = 6
    while a**2 * (y_i - 0.5) > b**2 * (x_i + 1):
        if len_dash > 3:           
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 6
        drawPoint(x - x_i, y - y_i)
        drawPoint(x + x_i, y - y_i)
        if P < 0:
            P += b**2 * (2 * x_i + 3)
        else:
            P += b**2 * (2 * x_i + 3) + a**2 * (-2 * y_i + 2)
            y_i -= 1
        x_i += 1

    Q = b**2 * (x_i + 0.5)**2 + a**2 * (y_i - 1)**2 - a**2 * b**2
    while y_i >= 0:
        if len_dash > 3:           
            drawPoint(x + x_i, y + y_i)
            drawPoint(x - x_i, y + y_i)
        len_dash -= 1
        if len_dash == 0:  
            len_dash = 6
        drawPoint(x - x_i, y - y_i)
        drawPoint(x + x_i, y - y_i)
        if Q < 0:
            Q += b**2 * (2 * x_i + 2) + a**2 * (-2 * y_i + 3)
            x_i += 1
        else:
            Q += a**2 * (3 - 2 * y_i)
        y_i -= 1

def input_table(root):
    input = Frame(root, bd=2, height=720, width=300, relief=SOLID)
    input.grid(row=0, column=0, padx=20)

    text = Label(input, text='INPUT', font=('Arial', 12, 'bold'), fg='blue')
    text.grid(row=0, column=0, columnspan=2, pady=10)

    lblX = Label(input, text='x', font=("Arial", 10, "bold"))
    lblX.grid(row=1, column=0)
    txtX = Entry(input, bd=2)
    txtX.insert(0, "0")
    txtX.grid(row=1, column=1, pady=5)
    
    lblY = Label(input, text='y', font=("Arial", 10, "bold"))
    lblY.grid(row=2, column=0)
    txtY = Entry(input, bd=2)
    txtY.insert(0, "0")
    txtY.grid(row=2, column=1, pady=5)

    lblA = Label(input, text='a', font=("Arial", 10, "bold"))
    lblA.grid(row=3, column=0)
    txtA = Entry(input, bd=2)
    txtA.grid(row=3, column=1, pady=5)

    lblB = Label(input, text='b', font=("Arial", 10, "bold"))
    lblB.grid(row=4, column=0)
    txtB = Entry(input, bd=2)
    txtB.grid(row=4, column=1, pady=5)

    btnHinhTron = Button(input, text='HÌNH ELLIPSE NÉT KHUẤT', padx=15, pady=10, 
                    command=lambda: drawHinhEllipse(int(txtX.get()), int(txtY.get()), int(txtA.get()), int(txtB.get())),
                    bg="#3399FF", fg="white", font=("Arial", 9, "bold"))
    btnHinhTron.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

def draw_table(root):
    draw = Frame(root, bd=2, height=670, width=800, relief=SOLID)
    draw.grid(row=0, column=1, padx=20, pady=20)

    canvas = Canvas(draw, width=800, height=670)
    canvas.pack()

    screen = turtle.TurtleScreen(canvas)
    screen.screensize(700, 900)
    screen.tracer(0)

    global p #Vẽ trục
    p = turtle.RawTurtle(screen)
    p.hideturtle()
    drawOxy()

    global t #Vẽ điểm
    t = turtle.RawTurtle(screen) 
    t.hideturtle()

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

def main():
    root = Tk()
    root.title('BÀI TẬP 4')
    root.minsize(1280, 720)
    input_table(root)
    draw_table(root)
    root.mainloop()

if __name__ == "__main__":
    main()