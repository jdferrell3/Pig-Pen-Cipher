# Pig Pen Writer
from turtle import Turtle
import turtle

AllLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NoDots = ["a","b","c","d","e","f","g","h","i"]
WithDots = ["j","k","l","m","n","o","p","q","r","w","y","z","x"]
Lefts = ["b","c","e","f","h","i","k","l","n","o","q","r"]
Rights = ["a","b","d","e","g","h","j","k","m","n","p","q"]
Bottoms = ["a","b","c","d","e","f","j","k","l","m","n","o"]
Tops = ["d","e","f","g","h","i","m","n","o","p","q","r"]
Diagonal = ["s","t","u","v"]
DiagonalDots = ["w","x","y","z"]

fontSize = 0.5

OUTFILE = 'pigpen.ps'

class PigPenEncoder():
    def __init__(self, save_file=False, outfile=OUTFILE):
        self.save_file = save_file
        self.outfile = outfile
        self.turtle = Turtle()
        self.InitialiseTurtle()

    def InitialiseTurtle(self):
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.pensize(3)
        self.turtle.color('black')

    def PenGoto(self, loc):
        self.turtle.penup()
        self.turtle.goto(loc)
        self.turtle.pendown()

    def Left(self, locx, locy):
        self.PenGoto((locx, locy))
        self.turtle.setheading(90)
        self.turtle.forward(40*fontSize)

    def Right(self, locx, locy):
        self.PenGoto((locx+40*fontSize, locy))
        self.turtle.setheading(90)
        self.turtle.forward(40*fontSize)

    def Bottom(self, locx, locy):
        self.PenGoto((locx,locy))
        self.turtle.setheading(0)
        self.turtle.forward(40*fontSize)

    def Top(self, locx, locy):
        self.PenGoto((locx,locy+40*fontSize))
        self.turtle.setheading(0)
        self.turtle.forward(40*fontSize)

    def LeftD(self, locx, locy):
        self.PenGoto((locx,locy+20*fontSize))
        self.turtle.setheading(90-63.43)
        self.turtle.forward(44.72*fontSize)
        self.PenGoto((locx,locy+20*fontSize))
        self.turtle.setheading(-90+63.43)
        self.turtle.forward(44.72*fontSize)

    def RightD(self, locx, locy):
        self.PenGoto((locx+40*fontSize,locy+20*fontSize))
        self.turtle.setheading(90+63.43)
        self.turtle.forward(44.72*fontSize)
        self.PenGoto((locx+40*fontSize,locy+20*fontSize))
        self.turtle.setheading(-90-63.43)
        self.turtle.forward(44.72*fontSize)

    def BottomD(self, locx, locy):
        self.PenGoto((locx+20*fontSize,locy))
        self.turtle.setheading(63.43)
        self.turtle.forward(44.72*fontSize)
        self.PenGoto((locx+20*fontSize,locy))
        self.turtle.setheading(116.57)
        self.turtle.forward(44.72*fontSize)

    def TopD(self, locx, locy):
        self.PenGoto((locx+20*fontSize,locy+40*fontSize))
        self.turtle.setheading(-63.43)
        self.turtle.forward(44.72*fontSize)
        self.PenGoto((locx+20*fontSize,locy+40*fontSize))
        self.turtle.setheading(180+63.43)
        self.turtle.forward(44.72*fontSize)

    def Square(self, mode, locx, locy):
        if "left" in mode:
            self.Left(locx, locy)
        if "right" in mode:
            self.Right(locx, locy)
        if "bottom" in mode:
            self.Bottom(locx, locy)
        if "top" in mode:
            self.Top(locx, locy)
        if "deft" in mode:
            self.LeftD(locx, locy)
        if "dot" in mode:
            self.BottomD(locx, locy)
        if "dop" in mode:
            self.TopD(locx, locy)
        if "dight" in mode:
            self.RightD(locx, locy)

    def Circle(self, locx,locy):
        temp = self.turtle.pensize()
        self.PenGoto((locx+20*fontSize, locy+20*fontSize))
        self.turtle.pensize(10*fontSize)
        self.turtle.forward(0.01)
        self.turtle.pensize(temp)

    def main(self, string_to_encode):
        x = -300
        y = 250

        for i in string_to_encode:
            try:
                i = i.lower()
            except:
                None
            mode = ""
            if i in WithDots:
                self.Circle(x, y)
            if i in Lefts:
                mode+="left"
            if i in Rights:
                mode+="right"
            if i in Bottoms:
                mode+="bottom"
            if i in Tops:
                mode+="top"
            if i in ["s","w"]:
                mode+="dot"
            if i in ["v","z"]:
                mode+="dop"
            if i in ["t","x"]:
                mode+="dight"
            if i in ["u","y"]:
                mode+="deft"
            self.Square(mode, x, y)

            x += 50*fontSize
            if x >= 300:
                x = -300
                y -= 60*fontSize

        if self.save_file:
            # save to postscript file
            ts = self.turtle.getscreen()
            cv = ts.getcanvas()
            cv.postscript(file=self.outfile, colormode='color')

if __name__ == '__main__':
    import time
    msg = input("Enter the message to be displayed: ")
    p = PigPenEncoder(save_file=True)
    p.main(msg)
    time.sleep(5)
