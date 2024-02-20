defmodule Prime do
  # Function to check whether a number is prime or not
  def is_prime(1), do: false
  def is_prime(n) when n > 1, do: is_prime(n, 2)

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor), do: is_prime(n, divisor + 1)
end

# Main program
defmodule PrimeFinder do
  def main do
    # Input a number from the user
    IO.put("Enter a number: ")
    number = String.trim(IO.gets(""), :both) |> String.to_integer()

    # Check if the number is prime or not
    if Prime.is_prime(number) do
      IO.puts("#{number} is a prime number.")
    else
      IO.puts("#{number} is not a prime number.")
    end
  end
end

# Run the program
PrimeFinder.main()
