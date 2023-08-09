# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# time: O(n+m) because we need to iterate through both strings but not nested
# space: O(n+m) because we need to create 2 hash maps

# input: 2 strings
# output boolean
# Use hash map and create dictionaries for both strings
# iterate through both strings separately (not nested)
# for each string's dict key should be letter and value should be number of occurences
# if a letter is in the dictionary increment value by 1
# else add it to the dictionary
# compare both hash maps and if similar return true

# time: O(n+m) because you are iterating through both strings (not nested)
# space: O(n+m) because we created 2 hash maps

def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    hashA = dict()
    hashB = dict()

    for char1 in s1:
        # check if key is within hash map
        if char1 in hashA:
            hashA[char1] += 1
        else:
            hashA[char1] = 1

    for char2 in s2:
        if char2 in hashB:
            hashB[char2] += 1
        else:
            hashB[char2] = 1

    if hashA == hashB:
        return True
    else:
        return False

print(anagrams('restful', 'fluster')) # -> True

# If you use the built in counter method it will create a hash map similar to the above
from collections import Counter

def anagrams_counter(s1, s2):
    return Counter(s2)

print(anagrams_counter('restful', 'flus ter')) # -> True
