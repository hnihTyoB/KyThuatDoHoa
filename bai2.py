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

def drawLine(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    if dx > dy:
        P = 2 * dy - dx
        x, y = x1, y1
        while x != x2:
            drawPoint(x, y)
            if P < 0:
                P += 2 * dy
            else:
                P += 2 * dy - 2 * dx
                y += step_y
            x += step_x
    else:
        P = 2 * dx - dy
        x, y = x1, y1
        while y != y2:
            drawPoint(x, y)
            if P < 0:
                P += 2 * dx
            else:
                P += 2 * dx - 2 * dy
                x += step_x
            y += step_y

    drawPoint(x2, y2)

def drawHCN(x1, y1, x2, y2):
    t.clear()
    t.penup()
    t.goto(x1 * 5, y1 * 5)
    t.pendown()
    t.fillcolor('#ff9999')
    t.begin_fill()
    drawLine(x1, y1, x2, y1)
    drawLine(x2, y1, x2, y2)
    drawLine(x2, y2, x1, y2)
    drawLine(x1, y2, x1, y1)
    t.end_fill()

def drawNetDut(x1, y1, x2, y2):
    t.clear()
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    P = 2 * dy - dx  # P0
    len_dash = 6
    
    x, y = x1, y1
    
    while x != x2:
        if len_dash >= 3:
            drawPoint(x, y)
        len_dash -= 1

        if len_dash == 0:  
            len_dash = 6

        if P < 0:
            P += 2 * dy
        else:
            P += 2 * dy - 2 * dx
            y += step_y
        
        x += step_x

def drawChamGach(x1, y1, x2, y2):
    t.clear()
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    P = 2 * dy - dx  # P0
    len_dash = 7
    
    x, y = x1, y1
    
    while x != x2:
        if len_dash >= 4 or len_dash == 2:
            drawPoint(x, y)
        len_dash -= 1

        if len_dash == 0:  
            len_dash = 7

        if P < 0:
            P += 2 * dy
        else:
            P += 2 * dy - 2 * dx
            y += step_y
        
        x += step_x

def draw2ChamGach(x1, y1, x2, y2):
    t.clear()
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    P = 2 * dy - dx  # P0
    len_dash = 15
    
    x, y = x1, y1
    
    while x != x2:
        if len_dash >= 9 or len_dash == 6 or len_dash == 3:
            drawPoint(x, y)
        len_dash -= 1

        if len_dash == 0:  
            len_dash = 15

        if P < 0:
            P += 2 * dy
        else:
            P += 2 * dy - 2 * dx
            y += step_y
        
        x += step_x

def drawMuiTen(x1, y1, x2, y2):
    t.clear()
    drawLine(x1, y1, x2, y2)

    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2) ** 0.5
    ux, uy = dx / length, dy / length

    arrow_size = length / 10
    ax1, ay1 = x2 - arrow_size * (ux - uy), y2 - arrow_size * (uy + ux)
    ax2, ay2 = x2 - arrow_size * (ux + uy), y2 - arrow_size * (uy - ux)

    drawLine(x2, y2, int(ax1), int(ay1))
    drawLine(x2, y2, int(ax2), int(ay2))

def input_table(root):
    input = Frame(root, bd=2, height=720, width=300, relief=SOLID)
    input.grid(row=0, column=0, padx=20)

    text = Label(input, text='INPUT', font=('Arial', 12, 'bold'), fg='blue')
    text.grid(row=0, column=0, columnspan=2, pady=10)

    lblX1 = Label(input, text='x1', font=("Arial", 10, "bold"))
    lblX1.grid(row=1, column=0, padx=10)
    txtX1 = Entry(input, bd=2)
    txtX1.grid(row=1, column=1, padx=10, pady=5)
    
    lblY1 = Label(input, text='y1', font=("Arial", 10, "bold"))
    lblY1.grid(row=2, column=0, padx=10)
    txtY1 = Entry(input, bd=2)
    txtY1.grid(row=2, column=1, padx=10, pady=5)

    lblX2 = Label(input, text='x2', font=("Arial", 10, "bold"))
    lblX2.grid(row=3, column=0, padx=10)
    txtX2 = Entry(input, bd=2)
    txtX2.grid(row=3, column=1, padx=10, pady=5)
    
    lblY2 = Label(input, text='y2', font=("Arial", 10, "bold"))
    lblY2.grid(row=4, column=0, padx=10)
    txtY2 = Entry(input, bd=2)
    txtY2.grid(row=4, column=1, padx=10, pady=5)

    btnNetDut = Button(input, text='NÉT ĐỨT', padx=15, pady=10, 
                   command=lambda: drawNetDut(int(txtX1.get()), int(txtY1.get()), int(txtX2.get()), int(txtY2.get())),
                   bg="#FF4444", fg="black", font=("Arial", 9, "bold"))
    btnNetDut.grid(row=5, column=0, columnspan=2, pady=10)

    btnHinhChuNhat = Button(input, text='HÌNH CHỮ NHẬT', padx=15, pady=10, 
                            command=lambda: drawHCN(int(txtX1.get()), int(txtY1.get()), int(txtX2.get()), int(txtY2.get())),
                            bg="#FF8800", fg="black", font=("Arial", 9, "bold"))
    btnHinhChuNhat.grid(row=6, column=0, columnspan=2, pady=10)

    btnChamGach = Button(input, text='NÉT CHẤM GẠCH', padx=15, pady=10, 
                        command=lambda: drawChamGach(int(txtX1.get()), int(txtY1.get()), int(txtX2.get()), int(txtY2.get())),
                        bg="#FFCC00", fg="black", font=("Arial", 9, "bold"))
    btnChamGach.grid(row=7, column=0, columnspan=2, pady=10)

    btn2ChamGach = Button(input, text='NÉT 2 CHẤM GẠCH', padx=15, pady=10, 
                        command=lambda: draw2ChamGach(int(txtX1.get()), int(txtY1.get()), int(txtX2.get()), int(txtY2.get())),
                        bg="#33CC33", fg="black", font=("Arial", 9, "bold"))
    btn2ChamGach.grid(row=8, column=0, columnspan=2, pady=10)

    btnMuiTen = Button(input, text='MŨI TÊN', padx=15, pady=10, 
                    command=lambda: drawMuiTen(int(txtX1.get()), int(txtY1.get()), int(txtX2.get()), int(txtY2.get())),
                    bg="#3399FF", fg="black", font=("Arial", 9, "bold"))
    btnMuiTen.grid(row=9, column=0, columnspan=2, pady=10)

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
    root.title('BÀI TẬP 2')
    root.minsize(1280, 720)
    input_table(root)
    draw_table(root)
    root.mainloop()

if __name__ == "__main__":
    main()