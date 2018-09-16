import math

a = 1
b = 1

result = 0

while(b < 4000000):
    x = a+b
    a = b
    b = x

    if b%2 is 0:
        result+= b

print(result)

wait = input(' ')