# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough.

# input: head of list
# output: list of all values in linked list
# create variable for list
# create current variable to point to head
# while loop to iterate as long as current != none
# append each value to list
# return list variable

# time O(n) traverse through every node to get value
# space O(n) since we create a list with all values

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
def linked_list_values(head):
  result = []
  current = head

  while current != None:
    result.append(current.val)
    current = current.next

  return result

# recursive solution
def linked_list_recur(head):
  values = []
  fill_values(head, values)
  return values


def fill_values(head, values):
  if head == None:
    return

  values.append(head.val)
  fill_values(head.next, values)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
print(linked_list_recur(a)) # -> [ 'a', 'b', 'c', 'd' ]
