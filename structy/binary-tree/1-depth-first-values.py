# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

# Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# input: root of tree
# output: list of each value of tree in depth first order
# create a stack (list) and have root inside
# create values to hold list of values
# while loop to iterate while stack has value
# create current variable by popping off value in stack
# append value to values list
# if current.right exists append to stack
# if current.left exists append to stack
# return values

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative solution
# time O(n) since we iterate through each node
# space O(n) since we create list of all values
def depth_first_values(root):
    if root is None:
       return []

    values = []

    stack = [root]
    while stack:
       current = stack.pop()
       values.append(current.val)

       if current.right is not None:
          stack.append(current.right)
       if current.left is not None:
          stack.append(current.left)

    return values

# recursive solution (uses call stack)
def depth_first_values_recur(root):
   if root is None:
      return []

   left_val = depth_first_values_recur(root.left)
   right_val = depth_first_values_recur(root.right)
   return [root.val, *left_val, *right_val]

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

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
