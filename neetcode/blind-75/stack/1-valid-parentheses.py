# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# input: string
# output: boolean if input is valid

# create stack to check each char in string
# create hash_map to confirm that a closing parenthese will close an open
# for loop to iterate through each char in string
# if char is opening parentheses add to stack
# and add to hash map
# if char is closing parentheses check to see if top of stack is opening
# if it is pop off else return False
# outside loop return True

def isValid(s):
    stack = []
    hash_map = {')':'(','}':'{',']':'['}

    for char in s:
        if char in hash_map:
            if stack and stack[-1] == hash_map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)


    return True if not stack else False

s = "()[{}]"
print(isValid(s))
