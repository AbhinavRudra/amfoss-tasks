#include <iostream>

// Function to check whether a number is prime or not
bool isPrime(int num) {
    if (num <= 1) {
        return false;  // Not a prime number
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;  // Not a prime number
        }
    }

    return true;  // Prime number
}

int main() {
    int number;

    // Input a number from the user
    std::cout << "Enter a number: ";
    std::cin >> number;

    // Check if the number is prime or not
    if (isPrime(number)) {
        std::cout << number << " is a prime number." << std::endl;
    } else {
        std::cout << number << " is not a prime number." << std::endl;
    }

    return 0;
}
