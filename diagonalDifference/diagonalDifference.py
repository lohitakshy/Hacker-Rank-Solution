def diagonalDifference(arr):
    sum1=0
    sum2=0
    num_rows = len(arr)-1
    print(arr)
    for i in range(num_rows+1):
        sum1 = sum1 + arr[i][i]
        print(sum1)
    for i in range(len(arr)):
        sum2 = sum2 + arr[num_rows][i]
        num_rows = num_rows -1
        print(sum2)
    return abs(sum1 - sum2) 
