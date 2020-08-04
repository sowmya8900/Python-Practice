from itertools import product
l = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l.append(a)
l.append(b)
p = tuple(product(a,b))
for i in p:
    print(i, end = " ") 
