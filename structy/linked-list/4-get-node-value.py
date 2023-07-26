# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# input: head and index
# output: value of index or None
# create a current variable to hold node
# create a counter variable starting at 0
# while loop to iterate until current = none
# if counter == index return current.val
# increment counter plus 1
# reassign current to current.next
# outside of loop return None

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time O(n) because we iterate through each node
# space O(1) not storing in dict or list
def get_node_value(head, index):
    counter = 0
    current = head

    while current != None:
       if counter == index:
          return current.val

       counter += 1
       current = current.next

    return None

# recursive solution
# time O(n) because of recursive call
# space O(n) because adding each call to callstack
def get_node_value_recur(head, index):
    if head == None:
       return None

    elif index == 0:
       return head.val

    index -= 1
    return get_node_value_recur(head.next, index)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'
print(get_node_value_recur(a, 2)) # 'c'
