# input: nums array
# output: duplicate number in array

# init fast and slow pointer to nums[0]
# while True loop to iterate until break
# slow = nums[slow]
# fast = nums[nums[fast]]
# if slow == fast break
# slow = nums[0]
# while slow != fast:
# slow = nums[slow]
# fast = nums[fast]
# return fast


def find_duplicate(nums):

    fast = slow = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]

    return fast

print(find_duplicate([3,4,4,4,2]))
print(find_duplicate([1,1]))
print(find_duplicate([1,3,4,2,2]))
