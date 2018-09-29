def solve(a, b):
    count1 = list(map(lambda x,y: 1 if x > y else 0,a,b))
    count2 = list(map(lambda x,y: 1 if x < y else 0,a,b))
    x = [sum(count1),sum(count2)]
    return x
