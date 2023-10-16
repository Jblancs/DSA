# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# input: list of nums and target sum
# output: list of 2 indices that equal target
# create num_dict to hold index as value
# for loop to iterate through nums using range(len(nums))
# create diff to hold target minus num
# if diff in num_dict return [num_dict[diff], idx]
# if num not in num_dict add it

# time O(n) since we iterate through each num
# space O(n) since we create dictionary

def twoSum(nums, target):
    num_dict = {}

    for idx in range(len(nums)):
        diff = target - nums[idx]
        if diff in num_dict:
            return [num_dict[diff],idx]
        if nums[idx] not in num_dict:
            num_dict[nums[idx]] = idx

print(twoSum([3,2,4], 6))
# Output: [1,2]
