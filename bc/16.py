li = [[1,2,3,4],[5,6,7,8]]

n = int(input("number:"))
cnt = 0

for i in range(len(li)):
    for j in range(len(li[i])):
        if cnt == 1:
            break
        if n == li[i][j]:
            cnt += 1
            print("%d (은)는 %d행 %d열 에 있습니다."%(n,i+1,j+1))
if cnt != 1:
    print("존재하지 않는 수 입니다.")
