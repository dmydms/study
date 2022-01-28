# 리팩토링 필요

n = int(input())

test_tuples = []
for i in range(0, n):
    r, chars = input().split(' ')
    test_tuples.append((int(r), chars))

for (r, chars) in test_tuples: 
    [print(c * r, end='') for c in chars]
    print('')
