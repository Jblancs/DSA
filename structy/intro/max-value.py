# Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

# Solve this without using any built-in list methods.

# You can assume that the list is non-empty.

def max_value(nums):
#   negative infinity
  max_num = float('-inf')

  for num in nums:
    if num > max_num:
      max_num = num

  return max_num

# n = length of list
# time 0(n)
# space 0(1)
