def dcount(n):
    p = int(n*(n+1)/2)
    c = 0
    s = 1
    while p % 2 ==0:
        p = p/2
        c += 1
    s = c + 1
    i = 1
    while p != 1:
        i += 2
        c = 0
        while p % i == 0:
            p = p/i
            c += 1
        s *= c + 1
    return s
for i in range(10000,100000000):
    if dcount(i) > 500:
        print(int(i*(i+1)/2))
        break
