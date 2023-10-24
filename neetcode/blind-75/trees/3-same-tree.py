# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# input: 2 roots
# output: boolean if trees are identical

# create 2 stacks
# while loop to iterate while stacks have value
# create current_p and current_q by pop() from each stack
# if current_p != current_q return False
# if current_p.left exists add to queue
# repeat for each
# outside loop return True

def isSameTree(p, q):
    stack_p = [p]
    stack_q = [q]

    while stack_p and stack_q:
        current_p = stack_p.pop()
        current_q = stack_q.pop()

        if (current_p and not current_q) or (current_q and not current_p):
            return False
        if current_q and current_p:
            if current_p.val != current_q.val:
                return False

        if current_p:
            stack_p.append(current_p.left)
            stack_p.append(current_p.right)

        if current_q:
            stack_q.append(current_q.left)
            stack_q.append(current_q.right)

    return True
