items = {"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
total = 0

while(1):
    tem = input("제품명:")

    if tem == "":
        break
    elif tem == "라면":
        total += items["라면"]
    elif tem == "우유":
        total += items["우유"]
    elif tem == "콜라":
        total += items["콜라"]
    elif tem == "캔커피":
        total += items["캔커피"]
    elif tem == "과자":
        total += items["과자"]


print("total:",total)
