stringArr = []
intArr = []
stringArr = input("숫자를 여러 개 입력하세요 : ")

i,a=0,0

print("")

while True:
    
    if stringArr[i] == None:
        break

    else:
        a=int(stringArr[i])
        
        intArr.append(a)
##2019038003 고영민##
        if(a==0):
            print("")

        elif(a==1):
            print("♥")

        elif(a==2):
            print("♥♥")

        elif(a==3):
            print("♥♥♥")

        elif(a==4):
            print("♥♥♥♥")

        elif(a==5):
            print("♥♥♥♥♥")

        elif(a==6):
            print("♥♥♥♥♥♥")

        elif(a==7):
            print("♥♥♥♥♥♥♥")

        elif(a==8):
            print("♥♥♥♥♥♥♥♥")

        elif(a==9):
            print("♥♥♥♥♥♥♥♥♥")

        i+=1
