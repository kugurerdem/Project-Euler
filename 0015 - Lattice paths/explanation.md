# Math approach

	Assume you are at the point (0,0), now notice given any destination point (n, k) such that n, k >= 0, you have to go through n+k steps (considering you only go right and down). Of n+k steps, if you choose at which step you go to right for n times, the remaining steps otomatically becomes going down. Since we want to find the all possible paths, we can calculate the combination nC(n+k, n) which is, in this case, cN(40, 20) since n = 20 and k = 20.

cN(40, 20) = 137846528820
