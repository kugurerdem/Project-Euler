# Function that finds greatest common divisor
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# Function that finds least common multiple
def lcm(x,y):
    return (x * y) / gcd(x,y)

least_common_multiple = 1;

# lcm(a,b) = A -> lcm(A,c) = lcm(a,b,c)
for i in range(1,21):
    least_common_multiple = lcm(least_common_multiple, i)

print(least_common_multiple)
x = input(' ')