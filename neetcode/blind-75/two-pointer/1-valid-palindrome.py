# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.



# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# input: string
# output: boolean if string is palindrome
# create i pointer and assign to 0
# create j pointer and assign to str.length
# while loop to iterate while i < j
# if not s[i].isalnum() i += 1
# if not s[j].isalnum() j -= 1
# if s[i] != s[j] return False
# increment i += 1
# decrement j += 1
# return True

# time O(n) where n is the char in string
# space O(1) done inplace with pointers

def isPalindrome(s):
    s_lower = s.lower()
    i = 0
    j = len(s)-1

    while i < j:
        i_alpha = s_lower[i].isalnum()
        j_alpha = s_lower[j].isalnum()

        if not i_alpha:
            i += 1
        if not j_alpha:
            j -= 1

        if i_alpha and j_alpha and s_lower[i] != s_lower[j]:
            return False

        if i_alpha and j_alpha:
            i += 1
            j -= 1

    return True

# better solution is to reverse the string
def isPalindromeReverse(s):
    s1 = ""

    for char in s:
        if char.isalnum():
            s1 += i

    k = s1.lower()
    if k[::-1] == k: # reverses string
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s)) #true
print(isPalindromeReverse(s)) #true
