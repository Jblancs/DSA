# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root of binary tree
# output: list of average of each level
# create queue for breadth first traversal
# create result list
# create num_vals to count value at each level
# for loop to iterate until queue is empty
# if len(result) == level add index
# if level == 0 append root.val to result
# else loop through
# else add to existing index


def level_averages(root):
  pass # todo



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

level_averages(a) # -> [ 3, 7.5, 1 ]
