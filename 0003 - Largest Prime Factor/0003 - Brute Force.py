import math

n = 600851475143
largest_prime = 0

i = 1
while i < n:
    if n%i == 0:
        largest_prime = i
        n = n/i
    
    i = i+1

print(largest_prime)

x = input(' ')