"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

class Colour:
    red = 'red'
    green = 'green'
    blue = 'blue'
    yellow = 'yellow'
    black = 'black'

def move_to_origin():
    global t
    t = turtle.Turtle()

def move_to_position(x,y):
    move_to_origin()
    t.penup()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()

def make_wheel(radius, col):
    t.color(col)
    t.circle(radius)
    t.color(Colour.black)

def rectangle(): pass

def make_door(length, height, col):
    t.color(col)
    for i in range(2):
        t.forward(height)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.color(Colour.black)

def make_bonnet(x,y):
    pass

def make_boot(x,y):
    pass

def make_roof(x,y):
    pass

def make_car(wheel_base, wheel_radius, door_height):
    half_wheel_base = wheel_base/2

    move_to_position(-half_wheel_base, 0) # Front wheel
    make_wheel(wheel_radius, Colour.red)

    move_to_position(half_wheel_base + 2*wheel_radius, 0)  # Back wheel
    make_wheel(wheel_radius, Colour.blue)

    move_to_position(0, 0)
    make_door(half_wheel_base, door_height, Colour.blue)  # Front door

    move_to_position(half_wheel_base, 0)
    make_door(half_wheel_base, door_height, Colour.red)  # Back door


make_car(wheel_base=80, wheel_radius=20, door_height=40)
