def find_primes(n)
    primes = []
    (2..n).each do |num|
       is_prime = true
       (2..Math.sqrt(num)).each do |i|
         if num % i == 0
           is_prime = false
           break
         end
       end
       primes << num if is_prime
    end
    primes
   end
   
   n = gets.chomp.to_i
   primes = find_primes(n)
   puts "Prime numbers up to and including #{n} are: #{primes.join(', ')}"