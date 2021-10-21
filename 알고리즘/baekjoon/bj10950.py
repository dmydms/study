n = int(input())

sums = []
for i in range(0, n): 
    a, b = [int(n) for n in input().split(' ')]
    sums.append(a + b)

[print(s) for s in sums]