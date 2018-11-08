from sympy import isprime
s, r = 0, 2000000
while r!=0:
    r = r - 1
    if isprime(r):
        s = s + r
print(s)
