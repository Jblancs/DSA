# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

# input: head of linked list
# output: boolean if list contains exactly 1 unique value
# create current variable to hold node
# create value variable to hold head.val
# while loop to iterate until current = None
# if current.val is not value return False
# outside return True

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time: O(n) because we iterate through whole list
# space O(1)
def is_univalue_list(head):
    value = head.val
    current = head

    while current is not None:
       if current.val != value:
          return False
       current = current.next

    return True

# recursive solution
def is_univalue_list_recur(head, prev=None):
    if head == None:
       return True

    if prev is not None and head.val != prev:
       return False

    return is_univalue_list_recur(head.next, head.val)

a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

print(is_univalue_list(a)) # True
print(is_univalue_list_recur(a)) # True
