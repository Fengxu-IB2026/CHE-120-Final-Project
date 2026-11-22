"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

from random import *
from turtle import *

from freegames import vector

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    """Update object positions."""
    #adds gravity to the objects, dropping 5 pixels per frame
    bird.y -= 5

    #moves the obstacles three pixels to the left per frame
    for ball in balls:
        ball.x -= 3

  
    if randrange(10) == 0: #gives a 1-in-10 chance for each frame to generate a new obstacle
        y = randrange(-199, 199) #assigns a random y-value for the obstacle inside the range of the screen
        ball = vector(199, y) #stores a new coordinate for the obstacle
        balls.append(ball) #adds the new obstacle to the list balls

    while len(balls) > 0 and not inside(balls[0]): # checks that the list balls is not empty to prevent an error and then finds the oldest obstacle that is still 'inside' or otherwise on the screen
        balls.pop(0) #removes the oldest ball from the list so that there are not unlimited obstacles 

    if not inside(bird): #checks if the bird is still on the screen and if not ends the game
        draw(False)
        return

    for ball in balls: #checks the distance between the obstacles and the bird using the size of both to make sure they dont overlap or otherwise ends the game
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True) #keeps the game going otherwise
    ontimer(move, 50) #keeps the game moving


setup(420, 420, 370, 0) #create a 420x420 window at screen position (370, 0)
hideturtle() #hide the default turtle pointer
up() #prevent lines from being drawn between points
tracer(False) #
onscreenclick(tap) #call the functions
move()
done()
