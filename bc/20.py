def str2int(n):
    jud = str.isdigit(n)

    if jud == True:
        print("문자열이 숫자로만 입력되었습니다.")
        n = int(n)
        print(type(n))
        return n
    else:
        return None


a = input("문자열 입력:")

print(str2int(a))
