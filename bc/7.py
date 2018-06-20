def vsum(*n):
    total = 0
    for i in n:
        total += i
        print(i,end=" ")
        if i == n[-1]:
            break
        print("+",end=" ")

    print("=",total)


vsum(2,3,4,5)
