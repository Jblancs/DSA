# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# input: 2 roots
# output: boolean if 2nd root is subtree of 1st
# create same_tree helper function
# create stack for depth first trav on first tree
# while loop to iterate while stack has value
# create current with stack.pop()
# if current.val == subRoot.val create result and call same_tree helper
# return result

def same_tree(current, subRoot):
    if current is None and subRoot is None:
        return True
    if current is None or subRoot is None:
        return False

    if current.val != subRoot.val:
        return False

    left = same_tree(current.left, subRoot.left)
    right = same_tree(current.right, subRoot.right)
    return left and right

def isSubtree(root, subRoot) -> bool:
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()

        if current.val == subRoot.val:
            result = same_tree(current, subRoot)
            if result:
                return result

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return False
