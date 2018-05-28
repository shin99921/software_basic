div = 0

def div_qr(a,b):
    global div
    print("몫:",(a//b),"나머지:",(a%b))


a = int(input("정수1 :"))
b = int(input("정수2 :"))
div_qr(a,b)
