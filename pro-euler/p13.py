with open("data/p13.txt","r") as f:
    a = [f.readline() for i in range(100)]
s = 0
for i in range(100):
    a[i] = a[i][:-1]
    a[i] = int(a[i])
    s += a[i]

print (str(s)[:10])
