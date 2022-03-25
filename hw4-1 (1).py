import random

data = []


for i in range (0,5):
    data.append(hex(random.randrange(0,100)))
    
##고영민 2019038003##
    
print("정렬 전 데이터 : ", end=" ")
[print(num, end=" ") for num in data]

min = data[0];
temp = 0;
for i in range(0,4):
    for j in range(i+1,5):
        if(int(data[i],16) > int(data[j],16)):
            temp = data[j]
            data[j] = data[i]
            data[i] = temp

print("")
print("정렬 후 데이터 : ", end=" ")
[print(num, end=" ") for num in data]
