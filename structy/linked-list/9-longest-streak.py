# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

# input: head of linked list
# output: number of longest streak
# create current variable to hold node
# create value to hold current value
# create streak to hold current streak
# while loop to iterate until current is None
# if value == current.val increment streak += 1
# else reassign value to current.val
# reset streak to 1
# outside while loop return streak


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative solution
# time O(n) because we iterate through list
# space O(1)
def longest_streak(head):
    value = head.val
    streak = 0
    highest_streak = 0

    current = head
    while current is not None:
        if value != current.val:
          value = current.val
          streak = 0

        streak += 1

        if streak > highest_streak:
           highest_streak = streak

        current = current.next

    return highest_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a)) # 3
