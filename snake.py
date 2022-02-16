
import  time
from turtle import Turtle
from score import Score
game = Score()
start_coordinates = [(0, 0), (-20, 0), (-40, 0)]
LEFT=180
RIGHT=0
UP=90
DOWN=270
class Snake:
    def __init__(self):
        self.sequence = []
        # self.snakepart=[]
        self.snake_body()
        self.head=self.sequence[0]
        self.movement=1

    def add_block(self,body):
        new_sequence = Turtle(shape="square")
        new_sequence.color('white')
        new_sequence.penup()
        new_sequence.shapesize(stretch_wid=1, stretch_len=1)
        new_sequence.setpos(body)
        self.sequence.append(new_sequence)

    def snake_body(self):
        for body in start_coordinates:
            self.add_block(body)

    def snake_movement(self):
        for seg in range(len(self.sequence) - 1, 0, -1):
            new_x = self.sequence[seg - 1].xcor()
            new_y = self.sequence[seg - 1].ycor()
            self.sequence[seg].goto(new_x, new_y)
        return self.sequence

    def new_body(self):

        length=len(self.sequence)-1
        new_x = self.sequence[length - 1].xcor()
        new_y = self.sequence[length - 1].ycor()
        new_cord = (new_x, new_y)
        self.add_block(new_cord)

    def forward(self):
        if(self.movement==1):
            self.head.forward(20)
        else:

            game.game_over()


    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(180)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(0)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(90)

    def down(self):
         if(self.head.heading()!=UP):
             self.head.setheading(270)

    # def wall(self):
    #     if(self.head.xcor()==300 or self.head.xcor()==-300 or self.head.ycor()==-300 or self.head.ycor()==300):
    #         print("Game Over")
    #         self.movement = 0
