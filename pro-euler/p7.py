from sympy import isprime
i = 1
c = 0
while i:
    i+=1
    if isprime(i):
        c+=1
        if c == 10001:
            print(i)
            break

