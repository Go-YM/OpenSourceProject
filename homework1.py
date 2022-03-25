import random

count, countS, countSame, countSeq = 0, 0, 0, 0
arr = [0,0,0,0,0,0]

while True:

    count += 1

    for i in range(0, 6):
        arr[i]=random.randrange(1,7)

    for j in range(1, 7):

        if j not in arr:
            break

        countS += 1

    if countS == 6 :
        countSeq = 0
        
##2019038003 고영민##
        
    for k in range(0, 5):

        if arr[k] == arr[k + 1]:
            countSame += 1
        else:
            break

    if countSame == 5:
        break

    countS = 0
    countSame = 0

print("6개의 주사위가 모두 동일한 숫자가 나옴 --> %d %d %d %d %d %d" % (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]))
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 --> %d" % count)
print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 --> %d" % countSame)




