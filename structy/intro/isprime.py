def is_prime(n):

# Find out if a number is prime
# output: boolean indicating prime num
# We need to loop through each int from 1 to n
# Use for loop and range from 1 to n + 1
# Use module % in order to find out if n is divisible by each int
# if statement to return false if modulo == 0
# edge cases: n = 1 return false

  if n == 1:
    return False

  for int in range(2, n):
    mod = n % int
    if mod == 0:
      return False

  return True

# n = input number
# time = O(n)
# space: O(1)

# better way is to use sqrt
from math import sqrt, floor

def is_prime2(n):
  if n < 2:
    return False

  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

# n = input number
# time = O(sqrt(n))
# space: O(1)
