a, b = [int(n) for n in input().split(' ')]

if a > b: 
    print('>')
elif a < b: 
    print('<')
else:
    print('==')