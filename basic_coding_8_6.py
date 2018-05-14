engkor_dict = dict()

while(1):
    
    eng = input("eng:")
    kor = input("kor:")

    if eng == "":
        break
    
    engkor_dict[eng] = kor

print(engkor_dict)
