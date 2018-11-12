import time
s = time.time()
with open("data/p11.txt",'r') as d:
    a = [[d.read(3) for c in range(20)] for x in range(20)]
    a = [[int(x) for x in a[i]] for i in range(20)]

def dr(i, j):
    p = 1
    if i in range(17) and j in range(17):
        for u in range(4):
            p *= a[i + u][j + u]
            if p == 0:
                return 0
        return p
    else:
        return 0

def horizon(i, j):
        p = 1
        if j in range(17):
            for u in range(4):
                p *= a[i][j + u]
                if p == 0:
                    return 0
            return p
        else:
            return 0
def dl(i, j):
    p = 1
    if i in range(17) and j in range(3,20):
        for u in range(4):
            p *= a[i + u][j - u]
            if p == 0:
                return 0
        return p
    else:
        return 0

def dow(i, j):
    p = 1
    if i in range(17):
        for u in range(4):
            p *= a[i + u][j]
            if p == 0:
                return 0
        return p
    else:
        return 0

max = 1
for t in range(20):
    for tt in range(20):
        newmax = dl(t, tt) if max < dl(t, tt) else max
        max = newmax
        newmax = dr(t, tt) if max < dr(t, tt) else max
        max = newmax
        newmax = dow(t, tt) if max < dow(t, tt) else max
        max = newmax
        newmax = horizon(t, tt) if max < horizon(t,tt) else max
        max = newmax
print(newmax, "in time", time.time() - s)
