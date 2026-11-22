"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

#randrange helps decide when and where new obstacles appear.
#Turtle draws shapes on the game screen and handles mouse clicks.
from random import *
from turtle import *

#Uses vectors to store position of an object with x and y coordinates
from freegames import vector

#Bird starts at the origin or the center
bird = vector(0, 0)
#Empty list so balls/obstacles are not generated yet
balls = []


def tap(x, y):
    """Move bird up in response to screen tap."""
    #Moves the bird up by 30 units by the y component 
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    # An object's x and y coordinate must in range of (-200,200) to be in the playing area
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    #Removes the previous frame so objects dont leave a trail of clones behind
    clear()

    goto(bird.x, bird.y)
    #Draws the bird to be green if the player is still alive and red when the game ends
    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    #Sets the obstacles as black balls with diameter of 20 units
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')
    #Refreshes the screen after drawing each object
    update()


def move():
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
