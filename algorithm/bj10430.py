# TODO: map 이용해서 리팩토링하기

def calculate_expression0(a: int, b: int, c: int):
    return (a + b) % c

def calculate_expression1(a: int, b: int, c: int):
    return ((a % c) + (b % c)) % c 

def calculate_expression2(a: int, b: int, c: int):
    return (a * b) % c

def calculate_expression3(a: int, b: int, c: int):
    return ((a % c) * (b % c)) % c 

a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

print(calculate_expression0(a, b, c))
print(calculate_expression1(a, b, c))
print(calculate_expression2(a, b, c))
print(calculate_expression3(a, b, c))
