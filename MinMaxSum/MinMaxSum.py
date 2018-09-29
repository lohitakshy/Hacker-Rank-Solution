def miniMaxSum(arr):
    sum1 = sum(arr)
    max1 = sum1 - min(arr)
    min1 = sum1 - max(arr)
    print(min1,max1)
