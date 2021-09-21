n = int(input())

sums = [] 
for i in range(0, n):
    scores = [(len(n) ** 2 + len(n)) / 2 for n in input().split('X')]
    sums.append(sum(scores))

for s in sums: 
    print(int(s))