def MakePalindrome(first_Half):
    secondHalf = str(first_Half)[::-1]
    palindrome = int( str(first_Half) + str(secondHalf) )
    return palindrome

found = False
firstHalf = 999

while not found:
    palin = MakePalindrome(firstHalf)

    for i in range(999,99,-1):
        if palin % i == 0 and (palin / i) > 99 and  (palin / i) < 1000:
            print(palin)
            
            print("divisor one: ", (palin/i) )
            print("divisor two: ", i)

            found = True
            break

    firstHalf = firstHalf - 1

x = input(' ')

