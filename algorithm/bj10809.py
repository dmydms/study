s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet: 
    print(s.index(a), end=' ') if a in s else print(-1, end=' ')