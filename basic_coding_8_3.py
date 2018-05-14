def grade(n):
    if 90 <= n <= 100:
        print(n,":","A")
    elif 80 <= n < 90:
        print(n,":","B")
    elif 70 <= n < 80:
        print(n,":","C")
    elif 60 <= n < 70:
        print(n,":","D")
    else:
        print(n,":","F")



while(1):

    scor = int(input("학점을 입력해 주세요:"))

    if scor < 0 or scor >100:
        continue
    else:
        grade(scor)
        break
