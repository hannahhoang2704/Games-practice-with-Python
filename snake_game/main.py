from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

"""snake = Turtle(shape="square")
snake.color('white')
snake.shapesize(1,3)"""

"""
starting_position= [(0,0), (-20,0), (-40,0)]
segments = []
for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
"""

snake = Snake()
food = Food()
score = Score()


screen.listen()         #listen to any keystroke
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        #print('nom nom nom')
        score.score_increase()
        snake.extend()
        snake.change_color()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.gameover()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()








screen.exitonclick()