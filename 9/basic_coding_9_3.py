a = b = c = 1

def func1():
    a = b = c = 2

def func2():
    global a, b
    a = b = 3
    c = 3

print(a,b,c)
func1()
print(a,b,c)
func2()
print(a,b,c)
