import copy

s7seg_num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],
             [1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
s7seg_num_anode = copy.deepcopy(s7seg_num)

for i in range(len(s7seg_num_anode)):
    for j in range(len(s7seg_num_anode[0])):
        if s7seg_num_anode[i][j] == 1:
            s7seg_num_anode[i][j] = 0
        else:
            s7seg_num_anode[i][j] = 1

print("s7seg_num")
for i in range(len(s7seg_num_anode)):
    for j in range(len(s7seg_num_anode[0])):
        print(s7seg_num[i][j],end=" ")
    print()

print("\n")

print("s7seg_num_anode")
for i in range(len(s7seg_num_anode)):
    for j in range(len(s7seg_num_anode[0])):
        print(s7seg_num_anode[i][j],end=" ")
    print()        
