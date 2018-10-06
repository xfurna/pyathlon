# EXCLUSIVELY FOR THIS PROBLEM
# IT WON'TR GIVE CORRECT ANSWER IN TWO CASES (report back if there exist any more)
# 1. if the number denoted as n here, has two prime factors only except 2
# 2. if the number n is even
from math import sqrt
n = 600851475143
m = n
t = 0
for i in range(3,  int(sqrt(max)), 2) :
    if int(n%i) is 0 :
        t=n
        n=n/i
print(t)
