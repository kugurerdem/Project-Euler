# Brute Force Approach

We know that a + b + c should equal to 1000, so we can say that c = 1000 - a - b, and we also can say a < b < c. Given that equations it simply follows that,
a < b < 1000-b-a therefore 2a < 2b < 1000 therefore a < b < 500. So we don't have to brute force until our parameters reach 1000, 500 would work too.

