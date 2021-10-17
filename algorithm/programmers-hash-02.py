# 문제: 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인

# 요소들을 정렬하고, 인접한 요소들끼리만 비교해서 하나의 원소가 다른 번호의 접두어인 경우가 있는지 확인 
# TOOD: 인접한 요소들만 비교하면 안되는 경우 있을 수 있지 않나?
def solution(phone_book):
    phone_book = sorted(phone_book)

    for num0, num1 in zip(phone_book, phone_book[1:]):
        if num1.startswith(num0):
            return False
        
    return True

# 프로그래머스에서 잘못된 풀이 발견

# 잘못된 이유: 
# 🌟 이모지 다음 line의 for문은 
# 주소록에 들어있는 전화번호 하나(문자열)를 가지고 반복문을 도는 것을 의미함. 

# temp라는 변수를 하나 만들어서 문자를 더하고, 
# 1)temp가 hash_map에 있으면서, 2)전화번호와 같지 않은 요소를 찾게끔함.

# 예를들어 다음과 같은 배열이 있다고 했을때, 
# ['123', '456', '2567']
# '123'에 대해서 반복문을 돌면, 
# number_char == '1'일 때, temp == '1'이고, 
# hash_map에서 '1'이 있으면서, '1'이 '123'과 같지 않을 때
# answer을 False로 바꿔줌. 

# 요소들끼리 비교해야하는 것이지, 요소의 일부 문자들이 해시맵에 있는지 확인할 필요는 없음. 
def wrong_solution(phone_book):
    answer = True
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        temp = ""
        # 🌟
        for number_char in number:
            temp += number_char
            if temp in hash_map and temp != number:
                answer = False
    return answer


