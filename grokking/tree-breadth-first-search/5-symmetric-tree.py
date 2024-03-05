# input: root
# output: boolean

from collections import deque
def is_symmetric(root):
    queue = deque([])
    queue.append(root.left)
    queue.append(root.right)

    while queue:
        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.data != right.data:
            return False

        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True
