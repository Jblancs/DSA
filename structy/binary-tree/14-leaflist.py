# Write a function, leafList, that takes in the root of a binary tree and returns an array containing the values of all leaf nodes in left-to-right order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def leaf_list(root):
  pass # todo

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

leaf_list(a) # -> [ 'd', 'e', 'f' ]
