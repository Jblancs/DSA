# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

# input: head and target value
# output: boolean if target is in linked list
# create current variable to hold node
# while loop to iterate until current == None
# if target == current.val return True
# reassign current to current.next
# outside of loop return False

# time: O(n) since we iterate a max of each node
# space: O(1) since we did not store any values

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
def linked_list_find(head, target):
    current = head

    while current != None:
       if current.val == target:
          return True

       current = current.next

    return False

# recursive solution
# time O(n) for recursive calls
# space O(n) to store each call stack (worse than iterative)
def linked_list_find_recur(head, target):
    if head == None:
       return False

    # must be after None base case in case there is no head
    if head.val == target:
       return True

    return linked_list_find_recur(head.next, target)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "c")) # True
print(linked_list_find_recur(a, "c")) # True
