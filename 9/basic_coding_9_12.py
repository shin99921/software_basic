import turtle as t

def keyup():
    t.forward(10)

def keydown():
    t.right(180)

def keyright():
    t.right(90)

def keyleft():
    t.left(90)

def keyreset():
    t.reset()

t.shape("turtle")    
s = t.Screen()
s.onkey(keyup,"Up")
s.onkey(keydown,"Down")
s.onkey(keyright,"Right")
s.onkey(keyleft,"Left")
s.onkey(keyreset,"r")
s.onkey(s.bye,"q")
s.listen()
