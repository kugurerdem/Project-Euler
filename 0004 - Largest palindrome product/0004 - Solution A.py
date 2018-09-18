palindrome = 0

def isPalindrome(string):
    for i in range( len(string) ):
        if( string[i] != string[len(string) - (i+1)]):
            return False
    return True


for i in range(100,1000):
    for j in range(100,1000):
        string = str(i*j)
        if isPalindrome(string) and int(string) > palindrome:
            palindrome = int(string)

print(palindrome)

x = input(' ')
