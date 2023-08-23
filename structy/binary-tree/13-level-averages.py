# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root of binary tree
# output: list of average of each level
# create stack for depth first traversal
# add tuple with node and level to stack
# create result list
# create average list
# while loop to iterate while stack contains a value
# unpack tuple to access node and level
# if level == len(result) add level to result
# else add to existing level
# if node.left exists add to stack
# same with right
# outside of while loop loop through result
# nest a loop to get average of values in each loop
# append average to average list
# return average list

from statistics import mean

def level_averages(root):
  stack = [(root, 0)]
  result_list = []
  average_list = []

  while stack:
    node, level = stack.pop()

    if level == len(result_list):
      result_list.append([node.val])
    else:
      result_list[level].append(node.val)

    if node.left:
      stack.append((node.left, level+1))
    if node.right:
      stack.append((node.right, level+1))

  for value_list in result_list:
    average_list.append(mean(value_list))

  return average_list

def level_averages_recur(root):
  levels = []
  fill_levels(root, levels, 0)

  averages = []
  for value_list in levels:
    averages.append(mean(value_list))

  return averages

def fill_levels(root, levels, level):
  if root is None:
    return

  if len(levels) == level:
    levels.append([root.val])
  else:
    levels[level].append(root.val)

  fill_levels(root.left, levels, level+1)
  fill_levels(root.right, levels, level+1)


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

print(level_averages(a)) # -> [ 3, 7.5, 1 ]
print(level_averages_recur(a)) # -> [ 3, 7.5, 1 ]
