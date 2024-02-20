function findPrimes(n) {
    const primes = [];
    for (let num = 2; num <= n; num++) {
       let isPrime = true;
       for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
         if (num % i === 0) {
           isPrime = false;
           break;
         }
       }
       if (isPrime) {
         primes.push(num);
       }
    }
    return primes;
   }
   
   const n = prompt("Enter a number: ");
   const primes = findPrimes(n);
   alert(`Prime numbers up to and including ${n} are: ${primes.join(', ')}`);