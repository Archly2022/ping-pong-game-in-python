import turtle
import os

arch = turtle.Screen()
arch.title('pong by Achilles')
arch.bgcolor('black')
arch.setup(width=1000, height=800)
arch.tracer(0)
os.system('afplay sos.wav&')

score_a = 0
score_b = 0
point_a = 0
point_b = 0

# Brick_a
brick_a = turtle.Turtle()
brick_a.speed(0)  # speed of animation
brick_a.shape('square')
brick_a.shapesize(stretch_wid=7, stretch_len=2)
brick_a.color('orange')
brick_a.penup()
brick_a.goto(-450, 0)

# brick_b
brick_b = turtle.Turtle()
brick_b.speed(0)
brick_b.shape('square')
brick_b.shapesize(stretch_wid=7, stretch_len=2)
brick_b.color('orange')
brick_b.penup()
brick_b.goto(450, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(2, 2, 2)
ball.color('orange')
ball.penup()
ball.goto(0, 0)
ball.x = 3
ball.y = 3

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('orange')
pen.penup()
pen.hideturtle()
pen.goto(0,280)
pen.clear()
pen.write('Player A Miss: 0  Player B Miss: 0', align='center', font=('courier', 34, 'italic'))


# move brick_a
def brick_a_up():
    y = brick_a.ycor()  # returns the y coordinates
    y += 30
    brick_a.sety(y)


def brick_a_down():
    y = brick_a.ycor()
    y -= 30
    brick_a.sety(y)


# move brick_b
def brick_b_up():
    y = brick_b.ycor()
    y += 30
    brick_b.sety(y)


def brick_b_down():
    y = brick_b.ycor()
    y -= 30
    brick_b.sety(y)


# keyboard binding

arch.listen()
arch.onkeypress(brick_a_up, 'Up')
arch.onkeypress(brick_a_down, 'space')
arch.onkeypress(brick_b_up, 'Left')
arch.onkeypress(brick_b_down, 'Down')

while True:
    arch.update()
    
    # move the ball
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)
    
