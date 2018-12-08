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
        self.draw = Turtle()
        self.InitialiseTurtle(self.draw)

    def InitialiseTurtle(self, t):
        t.speed(0)
        t.hideturtle()
        t.pensize(3)
        t.color('black')

    def PenGoto(self, loc, t):
        t.penup()
        t.goto(loc)
        t.pendown()

    def Left(self, locx,locy,t):
        self.PenGoto((locx,locy),t)
        t.setheading(90)
        t.forward(40*fontSize)

    def Right(self, locx,locy,t):
        self.PenGoto((locx+40*fontSize,locy),t)
        t.setheading(90)
        t.forward(40*fontSize)

    def Bottom(self, locx,locy,t):
        self.PenGoto((locx,locy),t)
        t.setheading(0)
        t.forward(40*fontSize)

    def Top(self, locx,locy,t):
        self.PenGoto((locx,locy+40*fontSize),t)
        t.setheading(0)
        t.forward(40*fontSize)

    def LeftD(self, locx,locy,t):
        self.PenGoto((locx,locy+20*fontSize),t)
        t.setheading(90-63.43)
        t.forward(44.72*fontSize)
        self.PenGoto((locx,locy+20*fontSize),t)
        t.setheading(-90+63.43)
        t.forward(44.72*fontSize)

    def RightD(self, locx,locy,t):
        self.PenGoto((locx+40*fontSize,locy+20*fontSize),t)
        t.setheading(90+63.43)
        t.forward(44.72*fontSize)
        self.PenGoto((locx+40*fontSize,locy+20*fontSize),t)
        t.setheading(-90-63.43)
        t.forward(44.72*fontSize)

    def BottomD(self, locx,locy,t):
        self.PenGoto((locx+20*fontSize,locy),t)
        t.setheading(63.43)
        t.forward(44.72*fontSize)
        self.PenGoto((locx+20*fontSize,locy),t)
        t.setheading(116.57)
        t.forward(44.72*fontSize)

    def TopD(self, locx,locy,t):
        self.PenGoto((locx+20*fontSize,locy+40*fontSize),t)
        t.setheading(-63.43)
        t.forward(44.72*fontSize)
        self.PenGoto((locx+20*fontSize,locy+40*fontSize),t)
        t.setheading(180+63.43)
        t.forward(44.72*fontSize)

    def Square(self, mode,locx,locy):
        if "left" in mode:
            self.Left(locx,locy, self.draw)
        if "right" in mode:
            self.Right(locx,locy, self.draw)
        if "bottom" in mode:
            self.Bottom(locx,locy, self.draw)
        if "top" in mode:
            self.Top(locx,locy, self.draw)
        if "deft" in mode:
            self.LeftD(locx,locy, self.draw)
        if "dot" in mode:
            self.BottomD(locx,locy, self.draw)
        if "dop" in mode:
            self.TopD(locx,locy, self.draw)
        if "dight" in mode:
            self.RightD(locx,locy, self.draw)

    def Circle(self, locx,locy,t):
        temp = t.pensize()
        self.PenGoto((locx+20*fontSize,locy+20*fontSize), self.draw)
        self.draw.pensize(10*fontSize)
        self.draw.forward(0.01)
        self.draw.pensize(temp)

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
                self.Circle(x,y,self.draw)
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
            self.Square(mode,x,y)

            x += 50*fontSize
            if x >= 300:
                x = -300
                y -= 60*fontSize

        if self.save_file:
            # save to postscript file
            ts = self.draw.getscreen()
            cv = ts.getcanvas()
            cv.postscript(file=self.outfile, colormode='color')

if __name__ == '__main__':
    import time
    msg = input("Enter the message to be displayed: ")
    p = PigPenEncoder(save_file=True)
    p.main(msg)
    time.sleep(5)
