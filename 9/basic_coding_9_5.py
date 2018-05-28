def div_qr(a,b):
    n1 = a//b
    n2 = a%b
    return (n1,n2)


a = int(input("정수1:"))
b = int(input("정수2:"))
n1,n2 = div_qr(a,b)
print("몫:",n1,"나머지:",n2)
