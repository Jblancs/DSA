# Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

# You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def bottom_right_value(root):
  pass # todo

a = Node(3)
b = Node(11)
c = Node(10)
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
#   11     10
#  / \      \
# 4   -2     1

print(bottom_right_value(a)) # -> 1
