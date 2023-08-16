# Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

# If the tree is empty, return -1.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# should mimic depth first traversal
# recursive solution is common for binary trees

def how_high(node):
  pass # todo

# recursive solution
# time O(n) since we go through n nodes
# space O(n) for each recursive call on stack
def how_high_recur(node):
  if node is None:
    return -1

  left = how_high_recur(node.left)
  right = how_high_recur(node.right)

  return 1 + max(left, right)

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

print(how_high(a)) # -> 2
print(how_high_recur(a)) # -> 2
