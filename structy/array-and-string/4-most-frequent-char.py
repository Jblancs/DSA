# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

# input: string
# output: most common letter
# create hash map to count each letter in the string
# create variable to hold letter and set to first letter
# if letter is in hash map increment by 1
# else add it to hash map
# iterate through hash map using dict.items() which return view obj as tuples in list
# set letter variable if value is higher than current letter
# return letter

# time: O(n+m) because you are iterating through the string and hash map
# space: O(n) because you are creating a hash map

def most_frequent_char(s):
    hash = dict()
    letter = s[0]

    for char in s:
        if char not in hash:
            hash[char] = 1
        else:
            hash[char] += 1

    for key, value in hash.items():
        if hash[letter] < value:
            letter = key

    return letter

# you can also use Counter
from collections import Counter

def most_frequent_char_counter(s):
    hash = Counter(s)
    letter = s[0]

    for key, value in hash.items():
        if hash[letter] < value:
            letter = key

    return letter

print(most_frequent_char('bookeeper')) # -> 'e'
