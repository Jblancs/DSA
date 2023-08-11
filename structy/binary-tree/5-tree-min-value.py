# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.

# input: root of tree
# output: min value
# create a queue
# create result to hold min and have it = float(inf)
# while queue to iterate until empty
# create current to hold popleft node
# if current.val < result result = current.val
# return result

from collections import deque
import math

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative solution
# time O(n) since we iterate through n nodes
# space O(n) since we create queue
def tree_min_value(root):
  result = math.inf
  queue = deque([root])

  while queue:
    current = queue.popleft()

    if current.val < result:
      result = current.val

    if current.right:
      queue.append(current.right)
    if current.left:
      queue.append(current.left)

  return result

# recursive solution

def tree_min_value_recur(root, result = math.inf):
  if root is None:
    return math.inf

  left = tree_min_value_recur(root.left, result)
  right = tree_min_value_recur(root.right, result)

  return min(root.val, left, right)


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
print(tree_min_value(a)) # -> -2
print(tree_min_value_recur(a)) # -> -2
