def seive(n):
    s = [True]*n
    s[1] = False
    for r in range(1, n):
        if s[r] is True:
            c = 2
            while r*c < n:
                s[r*c] = False
                c += 1
    sum = 0
    for r in range(n):
        if s[r]:
            sum += r
    return sum
print(seive(2000000))
