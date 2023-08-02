# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length
# of the input list.

# input: head of list, value and index
# output: head of linked list
# create new_node variable
# edge case: if index == 0 new_node.next = head and return new_node
# create current variable for traversing through list
# create previous variable to hold previous node
# create count variable
# while loop to iterate until current is None
# if count == index assign previous.next to new_node and new_node.next to current
# return head
# reassign previous to current
# reassign current to current.next
# increment count += 1
# outside loop return head

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time: O(index) since we traverse through the list
# space: O(1) since we only created pointer variables
def insert_node(head, value, index):
    new_node = Node(value)
    if index == 0:
       new_node.next = head
       return new_node

    count = 0
    current = head
    while current is not None:
       if index - count == 1:
          new_node.next = current.next
          current.next = new_node
          return head

       current = current.next
       count += 1

    return head

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(insert_node(a, 'x', 2))
print(insert_node_recur(a, 'x', 2))
# a -> b -> x -> c -> d
