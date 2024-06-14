import turtle as tk
import time

def draw_gallows():
    """Draws the gallows for the hangman"""
    tk.speed(0)
    tk.setup(1000, 2000, startx= 1000, starty= 3000)
    tk.penup()
    tk.goto(-100, -300)
    tk.pendown()
    tk.speed(1)
    tk.pensize(10)
    tk.forward(200)
    tk.penup()
    tk.goto(0, -290)
    tk.pendown()
    tk.lt(90)
    tk.forward(500)
    tk.rt(90)
    tk.forward(50)
    tk.rt(135)
    tk.forward(70)
    tk.backward(70)
    tk.lt(135)
    tk.forward(250)
    tk.rt(90)
    tk.forward(100)
    draw_position = tk.pos()
    time.sleep(3)

    return draw_position
