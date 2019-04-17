There are actually two solutions, one is brute force solution. And the other is mathematical approach.

# Brute force solution

We basically compute the next element of the sequence until we reach the point where it exceedes the limit (which is 10^999 in our case).

# Math solution

In [Wolfram's site](http://mathworld.wolfram.com/FibonacciNumber.html) there is a formula for fibbonacci sequence, this formula is called Binet's Fibonacci number formula: ![Binet's formula](http://mathworld.wolfram.com/images/equations/FibonacciNumber/Inline47.gif). Here, n gives the n_th value of the sequence. So we should find the least value of n that makes this expression bigger than 10^999.
