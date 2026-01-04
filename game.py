import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the alien"

alien = Actor("alien")
msg = ""

def draw():
    screen.clear()
    screen.fill("#ffafcc")

    alien.draw()
    screen.draw.text(msg, center = (400, 20), fontsize = 30, color = "black")

def update():
    pass

def place_alien():
    alien.x = randint(40, 450)
    alien.y = randint(50, 450)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        place_alien()
        msg = "BAM!"
    else:
        msg = "Miss"


place_alien()
pgzrun.go()