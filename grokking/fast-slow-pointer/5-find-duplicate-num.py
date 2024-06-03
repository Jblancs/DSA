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

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast


    # hash map solution ---------------
    # hash_map = {}

    # for idx in range(len(nums)):
    #     if nums[idx] in hash_map:
    #         return nums[idx]
    #     else:
    #         hash_map[nums[idx]] = idx


print(find_duplicate([1,1]))
print(find_duplicate([1,3,4,2,2]))
