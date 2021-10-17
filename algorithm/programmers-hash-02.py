# 문제: 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인

# 요소들을 정렬하고, 인접한 요소들끼리만 비교해서 하나의 원소가 다른 번호의 접두어인 경우가 있는지 확인 
# TOOD: 안되는 경우 있을 수 있지 않나?
def solution(phone_book):
    phone_book = sorted(phone_book)

    for num0, num1 in zip(phone_book, phone_book[1:]):
        if num1.startswith(num0):
            return False
        
    return True