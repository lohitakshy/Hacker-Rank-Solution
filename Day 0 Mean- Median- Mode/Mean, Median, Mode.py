total = int(input())
inputarr = input().split()
sum1 = 0
newint = []
model1 = {}
for i in range(total):
    sum1+=int(inputarr[i])
    newint.append(int(inputarr[i]))
    count = inputarr.count(inputarr[i])
    model1[int(inputarr[i])] = count        

print(round(sum1/total,1))
#print(model1[2184])
newint = sorted(newint)
if total%2 == 0:
    print(round((int(newint[total//2])+int(newint[(total//2) - 1]))/2,1))
else:
    print(round(newint[total//2],1))
max1 = max(model1.values())
index = [k for k, v in model1.items() if v == max1]
if len(index) == 1:
    print(index)
else:
    print(min(index))
