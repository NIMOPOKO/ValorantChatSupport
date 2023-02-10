import re
import time
print("文字を入力してください（アルファベットのみ）。記号は「!」，「?」，「 」（スペース）のみ使えます")
str = input()
space = "░"
length = len(str)
list =[[space for i in range(100)] for j in range(5)] 

f = open('moji.txt','r',encoding="UTF-8")
data = f.read()

def printValo():
    for y in range(5):
        for x in range(26):
            print(list[y][x],end="")
        print("\n",end="")

data2 = data.split('/')
#print(data2)
data3 = [[0]*3]*28 
for x in range(28):
     data3[x] = re.sub(r'(^\n)|(\n$)', '', data2[x]).split("\n")

#print(data3)
gyoucnt = 0
rawcnt = 0

def mojituika(cnt,moji):
    gyou = cnt*6+1
    list[1][gyou:gyou+5] = data3[moji][0]
    list[2][gyou:gyou+5] = data3[moji][1]
    list[3][gyou:gyou+5] = data3[moji][2]
    # list[2][gyou] = data3[moji][1]
    # list[3][gyou] = data3[moji][2]
flag = 0
alphasmall =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","?"]
alphabig =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","?"]
for x in range(length):
    if(str[x] == " "):
        gyoucnt+=1
    for n in range(28):
        if alphasmall[n] == str[x]:
            mojituika(gyoucnt,n)
            gyoucnt+=1
            break
        else:
            if alphabig[n] == str[x]:
                mojituika(gyoucnt,n)
                gyoucnt+=1
                break
    if gyoucnt == 4:
        printValo()
        gyoucnt=0
        list =[[space for i in range(100)] for j in range(5)]

if gyoucnt < 4 and gyoucnt != 0:
    printValo()

time.sleep(1000)