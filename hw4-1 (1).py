data = ['A37B','23CC','88D9','BB8F','3A9A']
intArr = [0,1,2,3,4,5,6,7,8,9]
dataArr=[]
count = 0
sumArr = 0

for i in data:
    for j in range(0,4):
        if i[j] not in intArr:
            continue
        else:
            count += 1

for i in data:
    for j in range(0,4):
        if i[j] not in intArr:
            continue
        else:
            if count != 0:
                sumArr += int(i[j])*10
            else:
                sumArr +=int(i[j])
    dataArr.append(sumArr)
    
print("정렬 전 데이터 : ", end=" ")
[print(num, end=" ") for num in data]

dataArr = sorted(dataArr)

print("")
print("정렬 후 데이터 : ", end=" ")
[print(num, end=" ") for num in dataArr]
