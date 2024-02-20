isPrime :: Integer -> Bool
isPrime n
  | n <= 1    = False  -- Not a prime number
  | otherwise = not $ any (\x -> n `mod` x == 0) [2..floor (sqrt (fromIntegral n))]

main :: IO ()
main = do
  -- Input a number from the user
  putStr "Enter a number: "
  input <- getLine
  let number = read input :: Integer

  -- Check if the number is prime or not
  if isPrime number
    then putStrLn $ show number ++ " is a prime number."
    else putStrLn $ show number ++ " is not a prime number."
