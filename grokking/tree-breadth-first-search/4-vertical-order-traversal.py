# input: root
# output: nested arrays based on column
# init queue using a deque and add in root,column tuple
# init hash_map to hold lists of each value in a column
# while queue has a value iterate
# unpack current and column from queue.popleft
# if hash_map does not have key column
# add that key with the value of an empty array
# outside if statement append current to hash_map[level]
# if current.left exists add to queue with column -1
# if current.right exists add to queue with column +1
# outside loop return list(hash_map.values())

from collections import deque
def vertical_order(root):
    if not root:
        return None

    queue = deque([(root, 0)])
    hash_map = {}

    left = 0
    right = 0

    while queue:
        current, col = queue.popleft()

        if col < left:
            left = col
        if col > right:
            right = col

        if col not in hash_map:
            hash_map[col] = []

        hash_map[col].append(current.data)

        if current.left:
            queue.append((current.left, col - 1))
        if current.right:
            queue.append((current.right, col + 1))

    return [hash_map[idx] for idx in range(left,right+1)]
