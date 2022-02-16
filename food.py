from turtle import Turtle
import random


from score import Score
score=Score()
class Food(Turtle):

    def __init__(self):
        self.rand_choice = []
        for i in range(-280, 281, 20):
            self.rand_choice.append(i)
        score.add_text()
        super().__init__()
        x = random.choice(self.rand_choice)
        y = random.choice(self.rand_choice)
        self.setpos(x=x, y=y)
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_len=.7, stretch_wid=.7)
        self.penup()
        self.speed("fastest")

    def random_food(self):
        x=random.choice(self.rand_choice)
        y=random.choice(self.rand_choice)
        self.setpos(x=x, y=y)
        score.score_add()
        print(x,y)

        # self.setpos(x=60, y=0)
    # def food_clear(self):
    #     self.clear()