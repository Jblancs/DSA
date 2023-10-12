# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# input: 2 strings
# output: boolean if 2 strings are anagrams

# for loop to create a hash map for each string
# compare both hash maps
# if equal return true else return false

# alternative import Counter

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        for char in s:
            if char not in hash_s:
                hash_s[char] = 0
            hash_s[char] += 1

        hash_t = {}
        for char in t:
            if char not in hash_t:
                hash_t[char] = 0
            hash_t[char] += 1

        return hash_s == hash_t


    def isAnagramAlt(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
