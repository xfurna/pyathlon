co=[0 for x in range(280)]
a=[0 for x in range(280)]
co[2]=1
for i in range(2,10):
    c = 0
    n=i
    while n != 1:
        if n%2==0:
            n = int(n/2)
            if i == 3:
                print("n",n,"cp",co[n])
            c = c+1
            if co[n]!=0:
                if i == 3:
                    print("as",co,"as",co[n]+c,"ss")
                co[i]=co[n]+c
                break
            a[n]=c
        else:
            n = 3*n +1
            c=c+1
            if co[n]!=0:
                co[i]=co[n]+c
                break
            a[n]=c
    for x in range(10):
        if a[x]!= 0:
            co[x]=c-a[x]
            a[x]=0
    print(c,co)
print(co)
