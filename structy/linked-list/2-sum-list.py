# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

# input: head of list
# output: sum of all node values
# create variable to hold total
# create current variable to hold node
# while loop to iterate until current == None
# add value to total variable
# reassign current to current.next
# return total

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
def sum_list(head):
  total = 0
  current = head

  while current != None:
    total += current.val
    current = current.next

  return total

# recursive solution
# time: O(n) for recursive call
def sum_list_recur(head):
  if head == None:
    return 0

  return head.val + sum_list_recur(head.next)


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
print(sum_list_recur(a)) # 19
