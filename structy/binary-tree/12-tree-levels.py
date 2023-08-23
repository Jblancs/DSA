# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# input: root of tree
# output: 2D list of vals at each level of tree

# iterative solution
# create a result list
# create a stack for a depth first traversal
# store root and level
# while loop to iterate while stack has value
# create current by popping off stack
# if index exists level < len(result) append else create
# if left exists append node and level
# same with right
# return result

# time: O(n) since we iterate through n nodes
# space O(n) since we create a list

def tree_levels(root):
  if root == None:
    return []

  result = []

  stack = [(root,0)]
  while stack:
#     unpacks tuple
    curr_node, curr_level = stack.pop()

    if curr_level == len(result):
      result.append([curr_node.val])
    else:
      result[curr_level].append(curr_node.val)

    if curr_node.right:
      stack.append((curr_node.right,curr_level+1))
    if curr_node.left:
      stack.append((curr_node.left, curr_level+1))

  return result

# recursive

def tree_levels_recur(root):
  levels = []
  fill_levels(root, levels, 0)
  return levels

def fill_levels(root, levels, num):
  if root == None:
    return

  if len(levels) == num:
    levels.append([root.val])
  else:
    levels[num].append(root.val)

  fill_levels(root.left, levels, num+1)
  fill_levels(root.right, levels, num+1)


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

tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
