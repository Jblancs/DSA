# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

# input: list of nums and target sum
# output: tuple of indicies adding to target sum
# create variable for hash map to get an O(n) time comp
# iterate through the list and subtract target sum from num at current index to get difference
# check if difference in within the hash map
# if not add key being the number and value being the index to that hash map
# if hash map contains difference as a key return tuple of index and current index

# time O(n) because we are iterating through the list
# space O(n) because we create a hash map dict


def pair_sum(numbers, target_sum):
    hash_map = dict()

    # use enumerate to pull index and value from list
    for idx, value in enumerate(numbers):
        diff = target_sum - value

        # diff in hash map searches in constant time since it is a dict
        if diff in hash_map:
            return tuple((hash_map[diff], idx))
        else:
            hash_map[value] = idx

print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)
