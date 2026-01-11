import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the alien"

change_color = False
alien = Actor("alien")
msg = ""

def draw():
    screen.clear()
    screen.fill("#ffafcc")

    alien.draw()
    screen.draw.text(msg, center = (400, 20), fontsize = 30, color = "black")
    if change_color:
        change_colour()
        alien.draw()
        screen.draw.text(msg, center = (400, 20), fontsize = 30, color = "black")

def update():
    pass

def place_alien():
    alien.x = randint(40, 450)
    alien.y = randint(50, 450)

def change_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(20, 255)
    screen.clear()
    screen.fill(color = (r, g, b))

def on_mouse_down(pos):
    global msg, change_color
    if alien.collidepoint(pos):
        place_alien()
        msg = "BAM!"
        change_color = True

    else:
        msg = "Miss"


place_alien()
pgzrun.go()