import operator

OriStr = ""

OriStr = input("원문\n")
StrLen = len(OriStr)

ary=[' ','\n','.',',']
sDic = {}

## 2019038003  고영민 ##

for i in range(len(OriStr)):
    if OriStr[i] in sDic:
        sDic[OriStr[i]] += 1

    elif OriStr[i] in ary:
        continue

    else:
        sDic[OriStr[i]] = 1

sList = sorted(sDic.items(), key=operator.itemgetter(1),reverse= True)

print("-------------------------")
print("문자\t\t빈도수")
print("-------------------------")

for i in range(len(sList)):
    print(f'{sList[i][0]}', '\t\t', f'{sList[i][1]}')
    
