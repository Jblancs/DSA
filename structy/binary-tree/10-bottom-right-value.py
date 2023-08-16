# Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

# You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root of tree
# right most value at lowest level
# create a queue using deque
# while loop to iterate until queue is empty
# create current by popleft
# if current.left exists add to queue before right
# queue will process left first meaning right will be processed last
# this is necessary because we are looking for the right most value
# return current.val

from collections import deque

def bottom_right_value(root):
  queue = deque([root])

  # create current outside although scoping for python works without it
  current = None

  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return current.val

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
