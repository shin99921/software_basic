data = []

while(True):
    st = input("string:")
    if st == "":
        break
    data.append(st)

for i in range(len(data)):
    print(data[i],end=" ")
