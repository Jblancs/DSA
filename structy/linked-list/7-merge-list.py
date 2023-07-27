# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

# input: head of 2 sorted linked lists
# output: 1 sorted linked list
# create a dummy variable for dummy node
# create a tail variable = dummy
# create a current_1 variable
# create a current_2 variable
# while loop to iterate until 1 or both current == None
# if current_1.val is less than current_2.val add it to tail
# else add current_2
# reassign the current used to next node
# outside loop return dummy.next

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time O(min(n,m)) since we iterate through shortest list
def merge_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    dummy = Node(None)
    tail = dummy

    while current_1 is not None and current_2 is not None:
      if current_1.val < current_2.val:
        tail.next = current_1
        current_1 = current_1.next
      else:
        tail.next = current_2
        current_2 = current_2.next

      tail = tail.next

    # assign left over nodes if any
    if current_1 is None:
      tail.next = current_2
    if current_2 is None:
      tail.next = current_1

    return dummy.next


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

print(merge_lists(a, q))
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
