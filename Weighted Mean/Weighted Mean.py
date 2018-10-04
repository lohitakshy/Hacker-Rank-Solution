leng = int(input())
wei  = input().split()
quan = input().split()
sum1 = 0
sum2 = 0
for i in range(leng):
    sum1 += int(wei[i])*int(quan[i])
    sum2 += int(quan[i])
print(round(sum1/sum2,1))
