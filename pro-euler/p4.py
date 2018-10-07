

def reve(t):
    if len(t) is not 0:                         
       return reve(t[1:]) + t[0]              
    else:
       return t

def fac(i):
    f = 0
    for u in range(1000, 100, -1):
        if (i%u == 0)*(i/u < 1000)*(i/u > 99):                                 
            f = 1
            break
    return f


for i in range(1000000, 100000, -1):
    s = str(i)
    if s == reve(s):
        if fac(i) is 1:
            break;
print(i)
