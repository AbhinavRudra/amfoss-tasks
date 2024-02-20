use std::io;

// Function to check whether a number is prime or not
fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;  // Not a prime number
    }

    for i in 2..=(num as f64).sqrt() as u32 {
        if num % i == 0 {
            return false;  // Not a prime number
        }
    }

    true  // Prime number
}

fn main() {
    // Input a number from the user
    println!("Enter a number: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let number: u32 = input.trim().parse().expect("Please enter a valid number");

    // Check if the number is prime or not
    if is_prime(number) {
        println!("{} is a prime number.", number);
    } else {
        println!("{} is not a prime number.", number);
    }
}
