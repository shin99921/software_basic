def calc(num1,num2,act="+"):
    if act == "+":
        print(num1,"+",num2,"=",num1+num2)
    elif act == "-":
        print(num1,"-",num2,"=",num1-num2)
    elif act == "*":
        print(num1,"*",num2,"=",num1*num2)
    elif act == "/":
        print(num1,"/",num2,"=",num1/num2)

n1 = int(input("n1:"))
n2 = int(input("n2:"))
ac = input("부호:")

calc(n1,n2,ac)
