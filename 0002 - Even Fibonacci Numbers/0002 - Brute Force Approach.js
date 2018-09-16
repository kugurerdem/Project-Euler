let a = 1; 
let b = 1;
let evenSum = 0;

while(b < 4000000){
	let x = a+b;
	a = b;
	b = x;
	
	if(b%2 == 0) evenSum+= b;
}

document.write(evenSum);