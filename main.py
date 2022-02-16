from turtle import Screen,Turtle
from snake import Snake
from food import Food
import time



# def border():
#     border_line=Turtle()
#     border_line.color('white')
#     border_line.width(10)
#     border_line.hideturtle()
#     border_line.setpos(x=-290,y=290)
#     border_line.forward(605)
# border()
def start():
    screen = Screen()
    screen.clear()
    screen.setup(width=605, height=605)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)
    is_on = True
    food = Food()
    snake = Snake()
    # screen.addshape('apple.png')
    screen.listen()
    while is_on:
        screen.update()
        time.sleep(.1)
         
        snake.snake_movement()
        snake.forward()
        screen.onkey(key='Up', fun=snake.up)
        screen.onkey(key='Down', fun=snake.down)
        screen.onkey(key='Left', fun=snake.left)
        screen.onkey(key='Right', fun=snake.right)
        # snake.wall()
        if (snake.head.distance(food) < 19):
            print("colllide")
            snake.new_body()
            food.random_food()
        for i in range(1, len(snake.sequence)):
            if (snake.head.distance(snake.sequence[i]) < 19):
                snake.movement = 0
        if (snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() <= -300 or snake.head.ycor() >= 300):
            snake.movement = 0
        if(snake.movement==0):
            screen.onkey(key='y', fun=start)
            screen.onkey(key='n', fun=exits)

def exits():
    exit(0)
start()


    

    

