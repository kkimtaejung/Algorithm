import math

a, b = map(int, input().split())

if a==2:
    a+=1
    print(2)
if a==1 and b>=2:
    a+=2
    print(2)
if b!=1:
    for i in range(a, b + 1):
        c = 0
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                c = 1
                break
        if c == 0 and i != 2:
            print(i)
        else:
            c = 0



