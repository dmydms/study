# todo:
# 1. blah 변수명 짓기
# 2. 식 일반화하기
a = int(input())
b = int(input())

num0 = a * (b % 10)
num1 = a * int((b % 100) / 10)
num2 = a * int(b / 100)

print(num0)
print(num1)
print(num2)
print(num0 + num1 * 10 + num2 * 100)