items = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
total = 0

while(True):
    tem = input("input:")

    if tem in items:
        total += items[tem]
        print("[%s:%d] > %d" %(tem,items[tem],total))
        
    if tem not in items:
        print(tem,"은 미등록 제품 입니다.")
        break



print("총 금액:",total)
        

