
# input: array of non-zero ints
# output: boolean if loop within array

# helper function to move through array:
# pass in pointer, value and size of nums array
# init result = (pointer + value) % size
# if result < 0 result += size

# helper function to see if cycle does not exist
# pass in array, prev_direct, pointer
# init curr_direct = nums[pointer] >= 0
# if (prev_direct != curr_direct) or (abs(nums[pointer] % len(nums)) == 0) return True
    # switches directions or loops over 1 idx
# else return False

# init size = len(nums)
# for i in range(size)
# init fast and slow to i
# init forward = nums[i] > 0
# while True loop to iterate until break
# slow = next_step()
# if is_not_cycle: break
# fast = next_step()
# if is_not_cycle: break
# repeat fast 1 more time
# if slow == fast return True
# outside loop return False

# time: On^2 since we nest an array to iterate over array
# space: O(1)

def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

def is_not_cycle(nums, prev_direct, pointer):
    curr_direct = nums[pointer] >= 0
    if (prev_direct != curr_direct) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False

def circular_array_loop(nums):
    size = len(nums)

    for i in range(size):
        slow = fast = i

        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True
    return False

print(circular_array_loop([1,3,-2,-4,1]))
print(circular_array_loop([2,1,-1,-2]))
print(circular_array_loop([5,4,-2,-1,3]))
