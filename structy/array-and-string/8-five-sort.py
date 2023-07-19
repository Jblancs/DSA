# Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

# input: list of nums
# output: list of nums with 5s moved to end

# create 2 point variables i and j to point at index at opposite sides of list
# while loop to iterate while i <= index j
# if list[j] = 5 decrement
# if list[i] != 5 increment
# if list[i] = 5 and list[j] != 5 swap the 2 indexes which is O(1) time
# return list

# time: O(n) because we iterate using a while loop
# space: O(1) since we did not create any new objects

def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[j] == 5:
            j -= 1

        # j should already been increment from above if
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]

        # if nums[i] isnt 5 it will increment
        else:
            i += 1

    return nums



print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5]

print(five_sort([5, 5, 5, 1, 1, 1, 4]))
# -> [4, 1, 1, 1, 5, 5, 5]
