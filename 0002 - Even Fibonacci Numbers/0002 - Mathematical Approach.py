# METHOD 2 : Mathematicial Approach
import math

# 1,1,'2',3,5,'8',13,21,'34'... 3*n th fibonacci numbers are even

def Fib(n):
    p = (1+math.sqrt(5)) / 2
    v = 1 - p

    return int( ( p**n - v**n ) / (p-v) )

# Finding the Nth fib number function

result = 0
N = 3

while result < 4000000:
    result += Fib(N)
    N+=3

print(result)

wait = input(' ')