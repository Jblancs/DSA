# Write a function, removeNode, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

# input: head of list and target value
# output: head of list with node containing value removed
# if head.val == target return head.next
# create a current variable for current node
# create previous variable to hold previous
# while loop to iterate until current is None
# if current.val == target, reassign prev.next = current.next
# return head
# previous = current
# current = current.next
# outside loop return head



class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time O(n) since we iterate through all nodes
# space O(1) sine we only have pointer variables
def remove_node(head, target_val):
    if head.val == target_val:
       head = head.next
       return head

    previous = None
    current = head
    while current is not None:
       if current.val == target_val:
          previous.next = current.next
          break

       previous = current
       current = current.next

    return head



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

print(remove_node(a, "c"))
# a -> b -> d -> e -> f
