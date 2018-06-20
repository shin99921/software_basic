a = int(input("주민등록번호 앞자리 6자를 입력해 주세요:"))
year = int(input("year:"))

age = a//10000
age = age+1900

reage = year-age

print("%d 살 입니다."% (reage+1))
