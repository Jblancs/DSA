# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root and target
# output: how many times target appears in tree
# create count variable to count number of times target appears
# create queue to perform a breadth first traversal
# while loop to iterate while queue has a value
# create current and popleft queue item
# if current.val == target increment count
# return count

# iterative solution
# time O(n) since we traverse through n nodes
# space O(n) since we create a queue of n nodes
from collections import deque

def tree_value_count(root, target):
  if root is None:
    return 0

  count = 0

  queue = deque([root])
  while queue:

    current = queue.popleft()

    if current.val == target:
      count += 1

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return count

# include count as an argument to keep track
# create base case to return count
def tree_value_count_recur(root, target):
  if root == None:
    return 0

  # need to still return 0 if no match
  match = 1 if root.val == target else 0

  left = tree_value_count_recur(root.left, target)
  right = tree_value_count_recur(root.right, target)

  return match + left + right


a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

print(tree_value_count(a,  6)) # -> 3
print(tree_value_count_recur(a,  6)) # -> 3
