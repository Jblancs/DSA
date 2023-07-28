# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

# input: head of linked list
# output: boolean if list contains exactly 1 unique value

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
    pass

a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

is_univalue_list(a) # True
