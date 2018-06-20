def pzn(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    elif n == 0:
        return 0


while(True):
    n = int(input("number input:"))
    print(pzn(n))
    if pzn(n) == 0:
        break
