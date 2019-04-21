// Initializing prime set
var prime = [2];
var num = prime[prime.length-1];
var sum_prime = 2;

var count = prime.length;

// we use the primes that is smaller than the current num
// in order to find new primes and add it to the sum
while(count < 2000000){
	
	var num = num + 1;
	
	var isPrime = true;
	for(var i = 0; i < prime.length; i++){
		if( num % prime[i] == 0){ 
			isPrime = false;
			break; 
		}
	}
	
	if(isPrime){
		sum_prime += num;
		prime.push(num);
	}
	
	count++
}

console.log(sum_prime);