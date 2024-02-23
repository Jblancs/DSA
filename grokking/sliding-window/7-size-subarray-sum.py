# input: target and nums array
# output: min length of contig subarray whos sum is greater than target

# init window_size to inf
# init start to 0 to track window
# init sum to 0 to track sum of window
# for loop to iterate through each idx in the array
# add each value at nums[idx] to the sum
# while sum is >= target and end - start + 1 < window size
# reassign window_size to end - start +1
# subtract nums[start] from sum
# increment sum += 1
# return window_size

def min_sub_array_len(target, nums):

    window_size = float("inf")
    start = 0
    sum = 0

    for end in range(len(nums)):
        sum += nums[end]

        while sum >= target:
            curr_size = end + 1 - start
            window_size = min(window_size, curr_size)
            
            sum -= nums[start]
            start += 1

    if window_size != float('inf'):
        return window_size

    return 0



print(min_sub_array_len(7, [2,3,1,2,4,3]))
