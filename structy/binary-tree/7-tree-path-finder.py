# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

# You may assume that the tree contains unique values.

# input: root and target val
# output: list containing path to target or None if target not in tree
# create base case if node is null return None
# create base case if node.val == target return [root.val]
# create left variable and recursive call
# if left is not None append root.val to left and return left
# same for right
# if both are none return None

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# reorder list
def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    # reverses list 3rd arg is step
    return result[::-1]

def _path_finder(root, target):
  if root == None:
    return None

  if root.val == target:
    return [root.val]

  left = _path_finder(root.left, target)
  print(left)
  if left is not None:
    # *left takes list and unpacks items so it runs O(n) making it O(n^2)
    # return [root.val, *left]
    left.append(root.val)
    return left

  right = _path_finder(root.right, target)
  if right is not None:
    # return [root.val, *right]
    # append will attach to end of list so need to reverse
    right.append(root.val)
    return right

  return None


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

print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]
