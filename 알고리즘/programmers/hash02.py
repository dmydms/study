# 문제: 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인

# 요소들을 정렬하고, 인접한 요소들끼리만 비교해서 하나의 원소가 다른 번호의 접두어인 경우가 있는지 확인 
# TOOD: 인접한 요소들만 비교하면 안되는 경우 있을 수 있지 않나?
def solution_zip(phone_book):
    phone_book = sorted(phone_book)

    for num0, num1 in zip(phone_book, phone_book[1:]):
        if num1.startswith(num0):
            return False
        
    return True

# 잘못된 풀이인줄 알았으나 잘못된게 아니였음.. 
# 코드는 잘못이 없다........... 
def solution(phone_book):
    answer = True
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        temp = ""
        for number_char in number:
            temp += number_char
            if temp in hash_map and temp != number:
                answer = False
    return answer


