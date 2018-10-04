import math
leng = int(input())
input1 = input().split()
sum1 = 0.0
newlist = []
for i in range(leng):
    sum1+=int(input1[i])
    newlist.append(int(input1[i]))
mean = sum1/leng
sum1 = 0.0
for i in range(leng):
    sum1+=(newlist[i] - mean)**2  
    
print(round(math.sqrt(sum1/leng),1))
