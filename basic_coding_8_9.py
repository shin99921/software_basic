import math

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def trunc(x):
    return math.trunc(x)


num = float(input("실수:"))

print("3.14 :",ceil(num))
print("3.14 :",floor(num))
print("3.14 :",trunc(num))
