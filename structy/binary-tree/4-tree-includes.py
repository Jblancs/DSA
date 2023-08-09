# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# input: root and target value
# output: boolean if target is in tree
# create stack
# while loop to iterate until stack is empty
# create current variable to hold node popped from stack
# if current.val == target return true
# if current.left exists add to stack
# if current.right exists add to stack
# outside of loop return false

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative solution
# time O(n) since we iterate through n nodes
# space O(n) since we use stack
def tree_includes(root, target):
  stack = [root]

  while stack:
    current = stack.pop()

    if current.val == target:
      return True

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return False

# recursive solution
# time O(n) since we recursively call for n nodes
# space O(n) since we have call stack 
def tree_includes_recur(root, target):
  if root == None:
    return False

  if root.val == target:
    return True

  return tree_includes_recur(root.left, target) or tree_includes_recur(root.right, target)


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

print(tree_includes(a, "e")) # -> True
print(tree_includes_recur(a, "e")) # -> True
