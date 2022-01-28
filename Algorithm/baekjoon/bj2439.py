# Q. 왜 이중 포문 안되는가?
# Q. print문 내부 출력 형식을 왜 +로 해야하는가? , 는 안되는가?

n = int(input())
[print(' ' * (n - i) + '*' * i) for i in range(1, n+1)]