# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9

# input: 2 heads of linked lists
# output: head of new list with vals added in reverse
# create dummy head variable
# create tail variable = dummy
# create carry variable = 0
# create current_1 for first list
# create current_2 for second list
# while loop to iterate while both currents are not None
# if current_1 and current_2 not None add the 2 values
# if sum is above 10 new_node.val = sum % 10 and carry = 1
# if current_1 is None new_node.val = current_2.val
# if current_2 is None new_node.val = current_1.val
# if current_1 is not None current_1 = current_1.next
# if current_1 is not None current_1 = current_1.next

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  dummy = Node(None)
  tail = dummy

  carry = 0
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val

    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10

    tail.next = Node(digit)
    tail = tail.next

    if current_1 is not None:
      current_1 = current_1.next

    if current_2 is not None:
      current_2 = current_2.next

  return dummy.next


def add_lists_recur(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val

  sum = val_1 + val_2 + carry
  next_carry = 1 if sum > 9 else 0

  digit = sum % 10
  result = Node(digit)

  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next

  result.next = add_lists_recur(next_1, next_2, next_carry)

  return result

#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

print(add_lists(a1, b1))
# 5 -> 7 -> 9
