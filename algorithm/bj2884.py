h, m = [int(n) for n in input().split(' ')]

if m > 44: 
    print(h, m - 45)
elif m <= 44 and h >= 1: 
    print(h - 1, m + 15)
else: 
    print(23, m + 15)

# Q. 왜 24의 나머지를 구하지?
# h, m = map(int, input().split())
# print((h+(m-45)//60)%24, (m-45)%60)