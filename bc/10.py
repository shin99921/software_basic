items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}

total = 0

while(True):
    tem = input("품목 입력:")

    if tem == "라면":
        total += items[tem]
    elif tem == "우유":
        total += items[tem]
    elif tem == "콜라":
        total += items[tem]
    elif tem == "캔커피":
        total += items[tem]
    elif tem == "과자":
        total += items[tem]
    elif tem == "":
        break
    else:
        print("없는 품목 입니다.")


print(total)
