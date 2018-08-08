# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms


def fib(): 
    a = 1
    c = 0
    s = 0
    while(c <  4000000):
      a, c = c, (a + c)
      if c%2 is 0:
          s = s + c
    print(s)
fib()
    

        



