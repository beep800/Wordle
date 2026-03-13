from turtle import Turtle

class word(Turtle):
    def __init__(self):
        super().__init__()
        self.word_to_guess="phone"
        self.nbguessleft=6
        self.guessused=0
        self.currentguess=[]

    def make_guess(self):
        for