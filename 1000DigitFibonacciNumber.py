fib = [1,1]

cnt = 2
lim = 10**999

while fib[1] < lim:
  tmp = fib[0] + fib[1]
  cnt = cnt + 1
  fib[0] = fib[1]
  fib[1] = tmp

print(cnt, "nth number is : ", fib[1])