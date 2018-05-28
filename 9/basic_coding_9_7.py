data = [1,2,3,4,5,6,7,8,9]
cnt = 0
a = int(input("찾을 값:"))

for i in range(len(data)):
    if a == data[i]:
        print("위치:",data[i]-1)
        break
    if i == len(data)-1:
        print("찾지 못함")
