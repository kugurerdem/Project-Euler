import math

g_ratio = (1+5**.5)/2.0 # golden ratio

#function that gives n_th value of fibonacci sequence
def fib(n): 
	return round(g_ratio**n / 5**.5)

lim = 10**999

print( fib(2) )
print( fib(5) )

# solution for n that gives fib(n) = 10**999
# hence the answer should be the 
# smallest greater integer then n
n = (math.log(lim) + math.log(5**0.5))/math.log(g_ratio) 

answer = int(n + 1)
print(answer)

# 