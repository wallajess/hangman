import turtle as tk
import time
from dataclasses import dataclass

@dataclass
class BodyPart:

    def draw():
        pass
        
@dataclass
class Head:

    def draw():
        tk.circle(40)

@dataclass
class Body:

    def draw():
        tk.forward(100)

@dataclass
class LeftLeg:
    
    def draw():
        tk.right(45)
        tk.forward(60)
        tk.left(45)
        
@dataclass
class RightLeg:

    def draw():
        tk.left(45)
        tk.forward(60)
        tk.right(45)
        
@dataclass
class RightArm:

    def draw():
        tk.left(45)
        tk.forward(60)
        tk.right(45)
@dataclass
class LeftArm:

    def draw():
        tk.right(45)
        tk.forward(60)
        tk.left(45)


def draw_hangman(attempts: int, word: str, draw_position: tuple, text_pos: tuple):
    """Draws the hangman step by step"""
    tk.pensize(5)
    tk.speed(1)
    if attempts == 1:
        tk.penup()
        tk.setposition(draw_position)
        tk.right(90)
        tk.pendown()
        Head.draw()
    elif attempts == 2:
        tk.penup()
        tk.setposition(draw_position)
        tk.left(90)
        tk.forward(80)
        tk.pendown()
        Body.draw()
    elif attempts == 3:
        tk.penup()
        tk.setposition(draw_position)
        tk.forward(180)
        tk.pendown()
        LeftLeg.draw()
    elif attempts == 4:
        tk.penup()
        tk.setposition(draw_position)
        tk.forward(180)
        tk.pendown()
        RightLeg.draw()
    elif attempts == 5:
        tk.penup()
        tk.setposition(draw_position)
        tk.forward(100)
        tk.pendown()
        RightArm.draw()
    elif attempts == 6:
        tk.penup()
        tk.setposition(draw_position)
        tk.forward(100)
        tk.pendown()
        LeftArm.draw()
        tk.penup()
        tk.setposition(text_pos)
        tk.pendown()
        tk.write(f"Sorry, you lost! The word was {word}", align = "left", font=("Arial", 12, "normal"))
    
    time.sleep(3)
