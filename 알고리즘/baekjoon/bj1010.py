# 조합, mCn = m!/(m-n)!n! 

def factorial(n):
    fact = 1
    for i in range(1, n+1): 
        fact = fact * i
    
    return fact

t = int(input())

cases = []
for i in range(0, t):
    a, b = [int(n) for n in input().split(' ')]

    if a == b: 
        cases.append(1)
    else: 
        cases.append(int(factorial(b) // factorial(b - a) // factorial(a)))

        
for c in cases: 
    print(c)