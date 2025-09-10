n = int(input())

c = 0
s = 0

for i in range(n):

    a = int(input())

    if i>=int(round(n*0.15)) and i<=int(round(n*0.85)):
        #if i>=int(round(n*0.85)):
        #    print(round(s/c))
        #    break
        c += 1
        s += a
        print(c,s, s/c)

print(round(s/c))