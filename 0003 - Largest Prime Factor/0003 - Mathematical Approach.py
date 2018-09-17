number = 600851475143
divisor = 2

while divisor ** 2 < number:
    if(number % divisor == 0):
        number = number / divisor
    else:
        divisor = divisor + 1

print(number)

x = input(' ')