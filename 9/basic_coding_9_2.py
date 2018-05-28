a = b = c = 1

def func():
    global a,b,c
    a = b = c = 2
    print("func:",a,b,c)

print("main:",a,b,c)
func()
print("main:",a,b,c)
