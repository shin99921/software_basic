engkor_dict = dict()

while(1):
    
    eng = input("eng:")

    if eng == "":
        break

    if len(engkor_dict) == 0:
        print("사전이 비어 있습니다.")

    if eng in engkor_dict:
        print(eng,":",engkor_dict[eng])
	continue
        
    else:
        print(eng,"단어가 사전에 없습니다, 사전에 추가합니다.")
    
    kor = input("kor:")
    
    engkor_dict[eng] = kor

print(engkor_dict)
