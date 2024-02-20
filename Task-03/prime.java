import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        int n = new Scanner(System.in).nextInt();
        List<Integer> primes = findPrimes(n);
        System.out.println("Prime numbers up to and including " + n + " are: " + primes);
    }

    public static List<Integer> findPrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int num = 2; num <= n; num++) {
            boolean isPrime = true;
            for (int i = 2; i <= Math.sqrt(num); i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(num);
            }
        }
        return primes;
    }
}