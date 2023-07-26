# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

# input: head
# output: new head of reversed linked list
# create prev variable to hold previous node
# create current variable to hold node
# create next variable to hold next node
# while loop to iterate until next is None
# reassign next to current.next
# reassign current.next to prev
# reassign prev to current
# outside of loop return current

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time O(n) because we traverse through each node
# space O(1) since we adjust nodes in place
def reverse_list(head):

    prev = None
    current = head
    next = head.next

    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next

    return prev

# recursive solution
def reverse_list_recur(head, prev=None):
  if head is None:
    return prev

  next = head.next
  head.next = prev
  
  return reverse_list_recur(next, head)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

# print(reverse_list(a)) # f -> e -> d -> c -> b -> a
print(reverse_list_recur(a, prev=None)) # f -> e -> d -> c -> b -> a
