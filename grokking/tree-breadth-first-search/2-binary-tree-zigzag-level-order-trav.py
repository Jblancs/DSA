# input: root
# output: array of arrays with each array rep certain level

# init a queue equal to deque with the root as the first element and level
# init result to empty array to hold values at each level
# while queue has a value:
# init current, level to queue to popleft
# if len of result < level + 1 that means there is no array yet
# append the empty array to result
# else append the current.data to the result[level]
# if level % 2 == 0
# if current.right exists add current.right
# repeat for left
# else append left then right
# return result

from collections import deque

def zigzag_level_order(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    result = []

    while queue:
        current, level = queue.popleft()

        if len(result) < level + 1:
            result.append([])

        result[level].append( current.data)

        if level % 2 == 0:
            if current.right:
                queue.append((current.right, level+1))
            if current.left:
                queue.append((current.left, level+1))

        else:
            if current.left:
                queue.append((current.left, level+1))
            if current.right:
                queue.append((current.right, level+1))

    return result
