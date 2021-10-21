# Q. 바로 형변환해서 a, b에 저장하는건 없나? 
# A. List Comprehension

a, b = [int(n) for n in input().split(' ')]

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)