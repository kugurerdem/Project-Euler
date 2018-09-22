# Function that checks if given number is prime or not
def isPrime(n):
    if (n <= 1) or (n % 2 == 0):
        return False
    
    div = 3
    while(div ** 2 <= n):
        if(n % div is 0):
            return False
        else: 
            div = div+2

    return True

count = 1
number = 1

''' We check if number is prime, if it is so we increase count's value by one. 
 We do this process until we reach 10001st prime number. We don't check for the even numbers, because
 we know they already cannot be a prime number. '''

while(count < 10001):
    number = number + 2
    if( isPrime(number) ):
        count = count + 1

print( number )

x = input(' ')

    