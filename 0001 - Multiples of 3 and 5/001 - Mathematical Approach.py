def SumDivisibleBy(n,p):
    return n*(p/n)*((p/n)+1)/2
	
print( SumDivisibleBy(3,999) + SumDivisibleBy(5,995) - SumDivisibleBy(15,990) )

x = input(' ')