# Brute Force 

We could simply try to divide n to its divisors from small numbers to big numbers, the last number that divides n is the largest prime factor of n. 

# Mathematical Approach

We can get any number by factoring prime numbers. Let 'A' be an any number, now we can express 'A' like: A = (p_1)^(n_1) * (p_2)^(n_2) *..* (p_x)^(n_x). Notice that p_3 > p_2 > p_1 etc. Now we can assume that 'A' will be bigger than (P_n)^2 whereas n is not the biggest prime factor of 'A'. Actually for any p_n^2, p_(n+1) * p_(n+2) will be bigger. One we got this we can easily fifgure it out that we can use 'A = A/divisor' because if there is more prime factors last we will continue this progress. When p_n^2 becomes greater than 'A', 'A' becomes the largest prime factor.
