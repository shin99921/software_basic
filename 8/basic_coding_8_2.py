st = list(input("문자열:"))

for i in range(len(st)):
    print(st[i],end="")

print()


for i in range(len(st)-1,-1,-1):
    print(st[i],end="")
