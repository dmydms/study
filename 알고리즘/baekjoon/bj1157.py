# solution 0.
word = input().upper()
uniq_chars = list(set(word))
cnt = [] 

for c in uniq_chars: 
    count = word.count(c)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else: 
    print(uniq_chars[cnt.index(max(cnt))])


# solution 1. 
# ord(문자): 문자의 ASCII 코드 반환
# chr(문자): 숫자에 대응하는 문자 반환
words = input().uppser()
letters = [words.count(chr(c)) for c in range(65, 91)]
m = max(letters)
if letters.count(m) == 1:
    print(chr(letters.index(m) + 65))
else: 
    print('?')

