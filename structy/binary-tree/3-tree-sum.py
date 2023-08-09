# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

# input: root of tree
# output: sum of all node values
# create stack for depth first traversal
# create a result to hold the sum
# while loop to iterate until stack is empty
# create current to hold node popped off of stack
# add current.val to result
# if current.left exists add to stack
# if current.right exists add to stack
# return result

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative solution
# time O(n) since we loop through each node
# space O(n) since we create stack
def tree_sum(root):
    if root is None:
       return 0
    
    stack = [root]
    result = 0

    while stack:
       current = stack.pop()
       result += current.val

       if current.right:
          stack.append(current.right)

       if current.left:
          stack.append(current.left)

    return result

# recursive solution
# time O(n) because of recursive call
# space O(n) because of stack
def tree_sum_recur(root):
    if root is None:
       return 0

    left = tree_sum_recur(root.left)
    right = tree_sum_recur(root.right)

    return root.val + left + right

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

print(tree_sum(a)) # -> 21
print(tree_sum_recur(a)) # -> 21
