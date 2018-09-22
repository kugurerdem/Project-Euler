import datetime

start = datetime.datetime.now()

def SquareOfTheSumOf(n):
    summation = 0
    for i in range(1,n+1):
        summation = summation + i
    return summation**2

def SumOfTheSquaresOf(n):
    summation = 0
    for i in range(1,n+1):
        summation = summation + i**2
    return summation

print('The answer is', ( SquareOfTheSumOf(100) - SumOfTheSquaresOf(100) ) )

finish = datetime.datetime.now()
delta = finish - start

print('Solution takes', delta.microseconds, 'ms')

x = input(' ')