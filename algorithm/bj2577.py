a = int(input())
b = int(input())
c = int(input())

multi_int2str = str(a * b * c)

for i in range(0, 10): 
    print(multi_int2str.count(str(i)))