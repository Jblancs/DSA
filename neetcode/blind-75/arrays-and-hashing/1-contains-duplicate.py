# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# input: list of nums
# output: boolean if a number apears twice in list

# for loop to create hash_map in order to count each num
# if hash_map does not contain num add it
# if hash_map contains num return True
# outside of loop return False

# time O(n) since we iterate through the array
# space O(n) since we create a hash map

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
