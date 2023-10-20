# Given the root of a binary tree, invert the tree, and return its root.



# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# input: root
# output: root of inverted tree

# create queue using deque
# while loop to perform breadth first
# create current and popleft from queue
# left = current.left
# right = current.right
# if left current.right = left
# queue.append current.right
# if right current.left = right
# queue.append current.left
# outside loop return root

def invertTree(root):
    if root == []:
        return []

    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current:
            left = current.left
            right = current.right

            current.right = left
            current.left = right

            if left:
                stack.append(current.right)
            if right:
                stack.append(current.left)

    return root



a = Node('a')
b = Node('b')
c = Node('c')

a.left = b
a.right = c

print(invertTree(a))
