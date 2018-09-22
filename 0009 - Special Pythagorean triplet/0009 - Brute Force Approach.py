summation = 1000

def productOfTriplets(summation):
    
    for a in range(int(summation/2)):
        for b in range(int(summation/2)):
            c = 1000-a-b
            if( a**2 + b**2 == c**2):
                return a * b * c
            

print( productOfTriplets(summation) )
x = input(' ')