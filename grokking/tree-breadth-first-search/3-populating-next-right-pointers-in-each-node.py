# input: root
# output: point next to immediate right node

# edge case if not root then return Null
# init queue using deque and add root,level tuple
# init prev_map to an empty object
# while queue has a value iterate
# unpack tuple to current and level equal to queue.popleft
# if level not in prev_map then add the key of level and value of current
# else if prev_map[level]: we are going to reassign prev_map[level].next to current
# also reassign prev_map[level] = current
# if current.right exists add node, level + 1
# repeat for left
# outside of loop return root

from collections import deque

def populate_next_pointers(root):

    if not root:
        return None

    queue = deque([(root, 0)])
    prev_map = {}

    while queue:
        current, level = queue.popleft()

        if level not in prev_map:
            prev_map[level] = current

        elif prev_map[level]:
            prev_map[level].next = current
            prev_map[level] = current

        if current.left:
            queue.append((current.left, level+1))

        if current.right:
            queue.append((current.right, level+1))

    return root
