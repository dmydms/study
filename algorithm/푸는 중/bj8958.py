n = int(input())

for i in range(0, n): 
    print([len(o) for o in input().split('X').remove('')])