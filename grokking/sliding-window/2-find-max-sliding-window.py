# input: list of nums and window size w
# output: list of highest value in each window
# initialize i = 0 for window
# while loop until i + w < len(nums) + 1
# initialize max to float('-inf')
# for loop iterate through win_idx from range(i, i+w)
# if nums[win_idx] > max reassign max to value
# outside for loop: if result
# if result[0] > max append max
# else appendleft
# else append max
# i += 1
# outside while loop return result

from collections import deque

def find_max_sliding_window(nums, w):

    i = 0
    result = deque()

    while (i + w) < (len(nums) + 1):
        max = float('-inf')

        for win_idx in range(i, i+w):
            if nums[win_idx] > max:
                max = nums[win_idx]

        if result:
            if result[0] > max:
                result.append(max)
            else:
                result.appendleft(max)
        else:
            result.append(max)

        i += 1

    return result

print(find_max_sliding_window([1,2,3,4,5,6,7,8,9,10], 3))

def clean_up(i, nums, current_window):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()
    return

def find_max_sliding_window_optimized(nums, w):
    if len(nums) == 1:
        return nums

    output = []
    window = deque()

    for i in range(w):
        clean_up(i, nums, window)
        window.append(i)

    output.append(nums[window[0]])

    for i in range(w, len(nums)):
        clean_up(i, nums, window)
        if window and window[0] <= (i-w):
            window.popleft()

        window.append(i)
        output.append(nums[window[0]])

    return output



print(find_max_sliding_window_optimized([1,2,3,4,5,6,7,8,9,10], 3))
