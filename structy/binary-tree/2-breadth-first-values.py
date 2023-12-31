# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

# input: root of tree
# output: list of all values in breadth order
# create a queue with root in it
# while loop to iterate until queue is empty
#

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque
# deque is a double ended queue and all operations that insert/remove from first and last run in constant O(1) time

def breadth_first_values(root):
    if root is None:
       return []

    values = []

    queue = deque([root])
    while queue:
      # popping from front of list runs O(n) time comp
      # current = queue.pop(0)

      # deque.popleft() runs in constant time
      current = queue.popleft()

      values.append(current.val)

      if current.left:
         queue.append(current.left)
      if current.right:
         queue.append(current.right)

    return values


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

print(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
