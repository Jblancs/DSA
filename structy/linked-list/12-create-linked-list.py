# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

# input: list of values
# output: head of linked list
# create head variable
# create prev variable to hold previous node
# for loop using enumerate to pull index and value tuple
# create new_node for each iteration
# if prev is not None prev.next = new_node
# else head = new_node
# prev = new_node
# outside loop return head

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# time O(n) to iterate through each value in list
# space O(n) to create each node
def create_linked_list(values):
    head = None
    prev = None

    for index, value in enumerate(values):
      new_node = Node(value)
      if index == 0:
          head = new_node
      else:
         prev.next = new_node

      prev = new_node
      print(new_node.val)

    return head

# solution using  dummy head (better)
def create_linked_list_while(values):
   dummy_head = Node(None)
   tail = dummy_head

   for val in values:
      tail.next = Node(val)
      tail = tail.next

   return dummy_head.next

print(create_linked_list(["h", "e", "y"]))
# h -> e -> y
