import operator

ttList = [('토마스', 5),('헨리', 8),('에드웟', 9),('에밀리', 5),('토마스', 4),('헨리', 7),('토마스', 3),('에밀리', 8),('퍼시', 4),('고든', 13)]

tDic, tList={},[]
temp = None
toRank, cuRank = 1,1
name,weight =0,0

rank = []
a = 0

for temp in ttList:
    name = temp[0]
    weight = temp[1]

    if name in tDic:
        tDic[name] += weight
    else:
        tDic[name] = weight

##고영민 2019038003##

print("기차 수송량 목록 ==> ", ttList)
print("------------------------")
tList = sorted(tDic.items(), key=operator.itemgetter(1), reverse = True)
print("기차\t총수송량\t순위 ")
print("------------------------")
print(tList[0][0],"\t",tList[0][1],"\t",cuRank)
for i in range(1,len(tList)):
    toRank +=1
    if tList[i][1] == tList[i-1][1]:
        pass
    else:
        cuRank = toRank

    print(tList[i][0],"\t",tList[i][1],"\t",cuRank)
