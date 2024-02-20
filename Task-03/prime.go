package main

import (
	"fmt"
	"math"
)

// Function to check whether a number is prime or not
func isPrime(num int) bool {
	if num <= 1 {
		return false // Not a prime number
	}

	// Check for factors up to the square root of the number
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false // Not a prime number
		}
	}

	return true // Prime number
}

func main() {
	// Input a number from the user
	var number int
	fmt.Print("Enter a number: ")
	fmt.Scan(&number)

	// Check if the number is prime or not
	if isPrime(number) {
		fmt.Printf("%d is a prime number.\n", number)
	} else {
		fmt.Printf("%d is not a prime number.\n", number)
	}
}
