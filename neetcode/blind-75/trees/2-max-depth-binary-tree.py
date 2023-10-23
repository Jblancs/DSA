# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# input: root
# output: max depth of tree
# create queue for breadth first trav
# in queue include a tuple containing node and level
# while loop to iterate while queue has value
# unpack tuple by popleft from queue
# if left or right exists add to queue with level incremented by 1
# return level

from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    
    queue = deque([(root, 1)])

    while len(queue) > 0:
        node, level = queue.popleft()

        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))

    return level

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')

a.left = b
a.right = c

print(maxDepth(a))
