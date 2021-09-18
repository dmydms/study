h, m = [int(n) for n in input().split(' ')]

# todo:
# 1. h == 0, m < 45 일 때,
# 2. m == 0 일 때, 
# 3. m < 45 일 때, 
# 4. 45 <= m < 60 일 때 

if h == 0 and m > 45: 
    h = 0
    m = m - 45

elif h == 0 and m < 45: 
    h = 23
    m = 60 - (45 - m)

elif m == 0:
    h -= 1

elif m < 45:
    h -= 1
    m = 60 - (45 - m)

else:
    m -= 45

print(f'{h} {m}')
