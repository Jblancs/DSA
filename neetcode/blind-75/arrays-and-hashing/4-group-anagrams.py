# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


# input: list of strings
# output: list of lists grouping anagrams together

from collections import Counter

# create result dict to hold groups of anagrams and use defaultdict(list) to have default value be a list
# for loop to iterate through strs
# create count list with 26 0s to represent each letter in alphabet
# purpose is to increment index for each char in string
# for loop to iterate through each char in str
# to get index use the ord built in
# **ord(character) returns the unicode point of that char (ex. 'a' === 97)
# calc the difference between ord(char) and ord('a') to get index in count list
# increment the value of that index by 1
# once count list is populated create key in result
# **lists CANNOT be keys so must change to a tuple
# result[tuple(count)].append(str)
# return result.values()

def groupAnagrams(strs):
    result = dict()

    for str in strs:
        count = [0] * 26
        for char in str:
            count_idx = ord(char) - ord('a')
            count[count_idx] += 1

        if tuple(count) not in result:
            result[tuple(count)] = []

        result[tuple(count)].append(str)

    return result.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs)) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# better solution is to sort the word and have that be used as the key in the result dict
def groupAnagramsSort(strs):
    result = {}

    for str in strs:
        sorted_word = ''.join(sorted(str)) # sorted sorts: tan > ant and nat > ant
        if sorted_word not in result:
            result[sorted_word] = []

        result[sorted_word].append(str)

    return result.values()

print(groupAnagramsSort(strs)) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
