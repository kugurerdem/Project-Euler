# Brute Force Approach

We can simply check for all numbers between 0 and 1000 and see if it can be divided by 3 or 5. If it can be divided than we simply add the number to summation.

# Mathematical Approach

Lets describ a function that sums integers dividable by any given number: SumDivisibleBy(n,p)
here n represents the first integer of our summation, for example at the series of 3+6+9+...+999 n equals to 3. And p represents the last integer in the summation, in this case "999" for example. As we can see any number in that series of summation must be dividibly by n, because they are already progressing with the n (3, 3+3, 3+3+3, 3+3+3+3....), so we can write our new equation like that: 3(1+2+3+4....+333). So if we could find the ast number divided by first number (lets say N=p/n) we could simply use this formula: n(N)(N+1)/2..

Having that formula now we can simply calculate the summation of arithmatic series. By the way i suggest you to see gauss's formula's proofs, it says where you try to calculate 1+2+3+4...+n you can simply use this formula n(n+1)/2. 

Now we can easily find the summation of numbers that are divisible by both 3 and 5: SumDivisibleBy(3,999) and SumDivisiblyBy(5,995) should give us the summations, however when we simply add this two results together we just ignore the numbers that are both dividable by 3 and 5, so we must reduce the summation of SumDivisiblyBy(15,990)

This should have give us the answer: SumDivisibleBy(3,999) + SumDivisiblyBy(5,995) - SumDivisiblyBy(15,995)
