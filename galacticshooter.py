import pgzrun
import random

WIDTH= 700
HEIGHT= 600

ship= Actor("ship.png")
op= Actor("enemies.png")

ship.pos= (WIDTH//2, HEIGHT- 60)
speed= 5
enemies= []
bullets= []
score= 0

enemies.append(op)
enemies[-1].x = 10
enemies[-1].y = 100

def draw():
    screen.clear()
    screen.fill("royal blue")
    ship.draw()
    screen.draw.text("Score = "+ str(score), (50,50))
    for e in enemies:
        e.draw()

def update():
    global score
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 40:
            ship.x= 40
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH- 40:
            ship.x= WIDTH - 40
    for e in enemies:
        e.y += 5
        if e.y >= HEIGHT:
            e.y= -100
            e.x = random.randint(40, WIDTH- 40)







pgzrun.go()