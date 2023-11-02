# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# input: root
# output: nested arrays for each level

# edge cases: if root is None return []
# create stack for traversal and initialize tuple of root node and level
# create result = []
# while stack iterate through each node
# unpack node and level with pop()
# if result[level] does not exist append [] to index
# result[level].append(node.val)
# if node.left exists add to stack
# repeat for right
# outside loop return result


def levelOrder(root):
    if root is None:
        return []

    stack = [(root, 0)]
    result = {}

    while stack:
        (node, level) = stack.pop()

        if level not in result:
            result[level] = []

        result[level].append(node.val)

        if node.right:
            stack.append((node.right, level+1))
        if node.left:
            stack.append((node.left, level+1))

    return result.values()
