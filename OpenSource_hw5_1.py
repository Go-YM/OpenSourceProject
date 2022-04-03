inStr, outStr = "",""

inStr = input("문자열을 입력하세요 : ")
length = len(inStr)

for i in range (0,length):
    if inStr[i].isupper() == True:
        outStr += inStr[i].lower()

## 2019038003   고영민 ##

    elif inStr[i].islower() == True:
        outStr += inStr[i].upper()

    else:
        outStr += inStr[i]

    

print("대소문자 반전시켜 출력 >>> %s"%outStr)
