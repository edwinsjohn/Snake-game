from turtle import Turtle
text=Turtle()
game_o=Turtle()
text.penup()
text.hideturtle()
text.setpos(x=0,y=260)
class Score:
    def __init__(self):
        self.score = 0

    def score_add(self):
        text.clear()
        self.score += 1
        self.add_text()

    def add_text(self):

        text.color('white')
        text.write(f"Score:{self.score}",font=("Verdana",
                                    20, "normal"),align="center")

    def game_over(self):

        game_o.penup()
        game_o.hideturtle()
        game_o.setpos(x=0,y=0)
        game_o.color('white')
        game_o.write("Game Over",font=("Verdana",
                                    40, "normal"),align="center")
        game_o.setpos(x=0, y=-100)
        game_o.write("Do you Want to Continue?", font=("Verdana",
                                        20, "normal"), align="center")
        game_o.setpos(x=0, y=-150)
        game_o.write("Yes(y) or No(n)", font=("Verdana",
                                                       15, "normal"), align="center")



        
        

