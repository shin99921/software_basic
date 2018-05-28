data = [[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]]
cnt = 0
a = int(input("찾을 값:"))

for i in range(len(data)):
    for j in range(len(data[0])):
        if a == data[i][j]:
            cnt += 1
            print("위치:",i+1,"행",j+1,"열")
            break
    if cnt == 1:
        break
if a != data[i][j]:
    cnt += 1
    print("찾지 못함")
