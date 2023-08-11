# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

# You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# recursive solution
# usually used for path problems
def max_path_sum(root):
  if root is None:
    return float("-inf")

  # if you are at a leaf node (no children)
  if root.left is None and root.right is None:
    return root.val

  max_left = max_path_sum(root.left)
  max_right = max_path_sum(root.right)

  return root.val + max(max_left, max_right)

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

max_path_sum(a) # -> 18
