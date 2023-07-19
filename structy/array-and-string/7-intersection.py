# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

# input: 2 lists of numbers
# output: list of all common numbers
# create a set and store one of the lists into it
# storing numbers in a set is O(1) time
# for loop to iterate over second list to check if it is included in set
# lookup is O(1) time
# if it is in the set store the number in the common list
# return common list

# time O(n+m) because we store each num in list a set and iterate through list b to compare
# spaace O(n) because we create a set and list

def intersection(a, b):
    common = list()
    set_a = set(a) # O(1) time to store each (similar to iterating and using .add)

    for num in b:
        # using the "in list" would make it n^2 but since its a set it is constant
        if num in set_a: # O(1) time to lookup in set
            common.append(num)

    return common

# better to solve with list comprehension
def intersection_list_comp(a, b):
    set_a = set(a)

    return [num for num in b if num in set_a]

print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]

# a = [ i for i in range(0, 50000) ]
# b = [ i for i in range(0, 50000) ]
# print(intersection(a, b)) # -> [0,1,2,3,..., 49999]
