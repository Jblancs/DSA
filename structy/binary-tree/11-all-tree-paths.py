# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root of binary tree
# output: 2D list containing paths root to leaf

# recursive solution
# base case if root == None return []
# base case if left and right is None return nested [[val]]

# time O(n) but could be a little more since each path contains more nodes that tree
# *array iterates through array
# space O(n) same as above

def all_tree_paths(root):
#   think of return and keep data type consistent
#   return a non-nested list because there are no paths
#   if you loop over an empty array it will NOT execute code in body
  if root is None:
    return []

#   this means that you are at leaf (no left/right)
  if root.left is None and root.right is None:
    return [[root.val]]

  paths = [] # gather all paths

#   should return nested paths starting with subtree (root = a)
  left_sub_path = all_tree_paths(root.left)
#   [[b,d],[b,e]] need to add a to front of each
  for sub_path in left_sub_path:
#   nesting *sub in loop makes it n^2 ish
    paths.append([root.val, *sub_path])

  right_sub_path = all_tree_paths(root.right)
  for sub_path in right_sub_path:
    paths.append([root.val, *sub_path])

  return paths

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

all_tree_paths(a) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]
