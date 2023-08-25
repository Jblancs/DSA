# Write a function, leafList, that takes in the root of a binary tree and returns an array containing the values of all leaf nodes in left-to-right order.

# input root of binary tree
# output list containing all leaves left to right
# create stack for depth first traversal
# create a result list
# while loop to iterate until stack empty
# create current node by popping off stack
# if current.left and current.right is None append val to result
# if current.right exists append to stack
# if current.left exists append to stack
# return result list

# time O(n) since we iterate through each node
# space is O(n) since we create a stack

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list(root):
  if root is None:
    return []

  result = []
  stack = [root]

  while stack:
    current = stack.pop()
    if current.left is None and current.right is None:
      result.append(current.val)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return result

def leaf_list_recur(root):
  leaves = []
  _leaf_list_recur(root, leaves)
  return leaves

def _leaf_list_recur(root, leaves):
  if root is None:
    return

  if root.left is None and root.right is None:
    leaves.append(root.val)

  _leaf_list_recur(root.left, leaves)
  _leaf_list_recur(root.right, leaves)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ]
print(leaf_list_recur(a)) # -> [ 'd', 'e', 'f' ]
