# 마주친 에러: 
# SyntaxError: unexpected EOF while parsing
# python3이 아니라 python2 로 실행함 
# python3에서 실행하는게 목적이였기 때문에 또 다시 에러를 마주쳤을 때 찾아보기로 함


a, b = [int(n) for n in input().split(' ')]

print(int(a) + int(b))