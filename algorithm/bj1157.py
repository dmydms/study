# todo: 
# 1. 입력받은 문자열(word) 대문자로 변환하기
# 2. word의 중복 문자를 제거하기, 왜? 탐색할 문자 종류 구하기 위해서  
# 3. 문자를 저장하는 변수(alphabet), 갯수(count)를 저장하는 변수 만들기
# 4. 문자열의 for loop를 돌면서 count함수로 총 갯수 구하기 
# 5-1. count 변수와 비교해서 더 크면 alphabe, count 변수 갱신하기 
# 5-2. 만약 동일하다면, alphabet을 ? 로 만들고 숫자는 그대로 두기 

word = input().upper()
set_word = set(word)

max_char_num = 0 
max_char = ''

for w in set_word:
    w_num = word.count(w)
    
    if max_char_num < w_num: 
        max_char_num = w_num
        max_char = w

    elif max_char_num == w_num and max_char != w : 
        max_char = '?'
    
    else:
        continue

print(max_char)