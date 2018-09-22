# Mathematical Approach

The question asks for the lcm of 1,2,3,4......,20. So we can handle this problem if we define a function that calculates largest common divisors of numbers. To do this, we can firstly define a function that gets greates common divisor, because as we know. lcm(a,b) = a*b / gcd(a,b)

```

/# Function that finds greatest common divisor
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

/# Function that finds least common multiple
def lcm(x,y):
    return (x * y) / gcd(x,y)

```

Also notice that 'lcm(a,b) = A -> lcm(A,c) = lcm(a,b,c)', so we can find the least common divisor in a loop by simple gettin lcd's of all the numbers.

```
for i in range(1,21):
    least_common_multiple = lcm(least_common_multiple, i)
```


By the way i reccomend you to see [this neat proof](https://www.whitman.edu/mathematics/higher_math_online/section03.03.html) of euclidean algorithm to find gcd.
