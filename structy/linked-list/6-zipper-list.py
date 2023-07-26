# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

# input: heads of 2 linked lists
# output: head of new zippered list
# create current_1 = head_1.next to traverse first list
# create current_2 = head_2 to traverse second list
# create tail = head_1 variable to hold last node in zippered list
# create count variable so you know which list to pull next node from
# while loop to iterate until current_1 and current_2 is None
# if count is even pull from list 2
# tail.next = current_2 if count is even
# reassign current_2 to current_2.next
# increment count up one
# repeat above steps for odds
# if either current is None it will exit loop
# if current_1 is None tail.next = current_1
# repeat above step for current_2
# this will handle if a list is longer than the other
# return head_1

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0

    while current_1 is not None and current_2 is not None:
      if count % 2 == 0:
        tail.next = current_2
        current_2 = current_2.next

      else:
        tail.next = current_1
        current_1 = current_1.next

      tail = tail.next
      count += 1

    if current_1 is not None:
      tail.next = current_1
    if current_2 is not None:
      tail.next = current_2
    return head_1



a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z
