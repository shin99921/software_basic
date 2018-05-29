import turtle as t
import time

default_shape = ["arrow","turtle","circle","square","triangle","classic"]
user_shape = ["/home/hong/Downloads/7s0.gif","/home/hong/Downloads/7s1.gif",
              "/home/hong/Downloads/7s2.gif"]

def addshape():
    for i in range(len(user_shape)):
        t.register_shape(user_shape[i])
    
def shape():
    for i in range(len(default_shape)):
        t.shape(default_shape[i])
        time.sleep(1)
    for j in range(len(user_shape)):
        t.shape(user_shape[j])
        time.sleep(1)


addshape()
shape()
