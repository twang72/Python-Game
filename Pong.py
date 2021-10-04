# A simple Pong game in Python
# Author: Yichen Wang

import turtle

window = turtle.Screen()
window.title("Pong by Yichen")
window.bgcolor("black")
window.setup(width = 800, height=600)

#the tracer funtion is used to speed up our game
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# the ball will move by 2 pixels
ball.dx = 2
ball.dy = 2

# Pen for scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "bold"))

# Score
score_a = 0
score_b = 0



# Function to move paddle A up
def paddle_a_up():
     y = paddle_a.ycor()
     y += 20
     paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
     y = paddle_a.ycor()
     y -= 20
     paddle_a.sety(y)

# Funtion to move paddle B up
def paddle_b_up():
     y = paddle_b.ycor()
     y += 20
     paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
     y = paddle_b.ycor()
     y -= 20
     paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_up, "Up")
window.onkey(paddle_b_down, "Down")


# Main game loop - every game needs this
while True:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        #reverse the direction
        ball.dy *= -1
    

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
    
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
    

    # when the ball touches paddles
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1 

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1   
