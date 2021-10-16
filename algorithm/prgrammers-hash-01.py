from collections import Counter

# 참가자와 완주자를 카운터 객체로 전달해서 
# 인자의 갯수가 몇개인지에 대한 정보를 담은 dictionary의 차를 통해 구하는 방법 
def solution_counter(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

# 참가자와 완주자의 해시 인덱스 값을 각각 더해서 차를 구하는 방법
def solution_hash(participants, completions):
    hash_idx = 0
    dic = {}
    
    for p in participants:
        dic[hash(p)] = p
        hash_idx += int(hash(p))

    for c in completions:
        hash_idx -= hash(c)

    return dic[hash_idx]

# 참가자와 완주자를 정렬한 다음, 같은 index의 값이 같은지 확인하며 구하는 방법
def solution_sort_zip(participants, completions):
    participants.sort()
    completions.sort()

    for p, c in zip(participants, completions):
        if p != c:
            return p
    return participants[-1]
