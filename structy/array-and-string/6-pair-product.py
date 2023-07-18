# Write a function, pairProduct, that takes in an array and a target product as arguments. The function should return an array containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

# input: list of nums and target product
# output: tuple of indicies
# create hash map variable to hold previous nums
# for loop to iterate over list of nums
# use enumerate to pull both value and indicies
# use modulo to see if target prod is divisible by current value
# if modulo = 0 calculate num and return index and current index in tuple
# add current value and index to hash map

# time: O(n) because we iterate through the list of nums
# space: O(n) because we created a hash map using dict

def pair_product(numbers, target_product):
    hash_map = {}

    # use enumerate to get tuple containing idx, num
    for idx, num in enumerate(numbers):
        quotient = target_product/num
        if quotient in hash_map:
            return tuple((hash_map[quotient], idx))
        hash_map[num] = idx



print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)
