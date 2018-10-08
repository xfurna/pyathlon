def fac(o, h):
    m = o
    if o > h:
        m = h
        x = 1
    for x in range(m, 0, -1):
        if o % x == 0 and h % x == 0:
            break   
    return x

def l(n, j):
    if n is not 1:
       j = n*j/fac(n, j)
       l(n-1, j)
    if n is 1:
       print(j)
    return 0;
l(20, 1)
    
