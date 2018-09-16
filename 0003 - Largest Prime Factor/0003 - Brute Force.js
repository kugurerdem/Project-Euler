let n = 600851475143;

let largest_prime = 0;

let divisor = 2;

while(divisor <= n){
    if(n % divisor == 0){
        largest_prime = divisor;
        n = n / divisor;
    } else{
        divisor++;
    }
}

console.log(largest_prime);