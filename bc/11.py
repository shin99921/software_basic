dict_engkor = dict()

while(True):
    eng = input("영어입력:")
    if eng == "":
        break
    elif eng in dict_engkor:
        print("영어단어가 이미 사전에 있습니다.")
        continue
    elif eng not in dict_engkor:
        print("영어단어 를 사전에 추가 합니다.")
        kor = input("단어의 뜻을 입력해 주세요:")
        dict_engkor[eng] = kor

print(dict_engkor)
