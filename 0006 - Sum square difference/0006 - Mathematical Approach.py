import datetime

start = datetime.datetime.now()

def SquareOfTheSumOf(n):
    return (n*(n+1)/2)**2

def SumOfTheSquaresOf(n):
    return n*(n+1)*(2*n+1) / 6

print('The answer is',  SquareOfTheSumOf(100) - SumOfTheSquaresOf(100) )

finish = datetime.datetime.now()
delta = finish - start

print('Solution takes', delta.microseconds, 'ms')

x = input(' ')