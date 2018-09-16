# Brute Force Approach

There is something that we should figure it out, we should generate and check fibonnaci series' numbers but we dont need to use a memory for each member of the series of fibonnacci. Lets remember the formula for fibonacci series n_th number: F_n = F_(n-1) + F_(n-2). So we only need to memorize the last two members of the fibonnaci series. We simply generate the next fibonacci number from the previous ones and than check if it is dividible by 2 or not.

# Mathematical Approach

Notice the pattern of fibonacci series: 1,'2',3,5,'8',13,21,'34'.. After '2' every thirth number is even. So if we have a function that determines fibonacci series' any given n_th number. We could simply check for F_n, F_(n+3), F_(n+6) etc. With this way we can simply reduce the iteration number by 3 times shorter than the previous one.

Our formula is to determine fibonacci series' any given n_th number can be formulated like this: 

```
def Fib(n):
    p = (1+math.sqrt(5)) / 2
    v = 1 - p

    return int( ( p**n - v**n ) / (p-v) )
 ```
    
