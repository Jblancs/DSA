# input: string s that represents DNA sub sequence and number k
# output: all contiguous substrings of length k that occur more than once or empty set if none

# create hash table to store substring
# initialize start and end to hold window
# while loop to iterate until end > len(s)
# init substring to hold string to add to hashmap
# if hash[substring] exists increment value by 1
# else add hash[substring] = 1
# increment start and end + 1
# outside loop init result = []
# iterate over hash and add each string with value > 1 to result

# time: O(k(n-k)) since we iterate over each string with length k and slice out k char
# space: O(k(n-k) since we create hashmap

def find_repeated_sequences(s, k):
    table = {}
    start = 0
    end = k

    while end <= len(s):
        substring = s[start:end]
        if substring in table:
            table[substring] += 1
        else:
            table[substring] = 1

        start += 1
        end += 1

    res = []
    for key in table:
        if table[key] > 1:
            res.append(key)

    return res

print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC", 8))
