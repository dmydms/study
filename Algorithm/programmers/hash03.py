from collections import Counter 

# 조합
def solution(clothes):
    answer = 1
    cloth_nums = Counter([c for _, c in clothes]).values()
    
    for n in cloth_nums:
        answer *= (n + 1)
    
    return answer - 1