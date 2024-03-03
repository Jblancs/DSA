# input: root
# output: string of values separated by level with :
# init deque with tuple containing node and level of node
# init result to empty array
# while loop to iterate while deque has a value
# init current to popleft of queue
# check if there is a value at result at index level by comparing length to level +1
# if there is not append ""
# add value to string at result[level] += ,current.value
# if current.left exists append to queue
# if current.right exists append to queue
# outside of loop
# return ":".join(result)


from collections import deque

def level_order_traversal(root):
    result = []
    if not root:
        return "None"

    queue = deque([(root, 0)])

    while queue:
        current, level = queue.popleft()

        if not len(result) == (level + 1):
            result.append(f"{current.data}")
        else:
            result[level] += f", {current.data}"

        if current.left:
            queue.append((current.left, level + 1))

        if current.right:
            queue.append((current.right, level + 1))

    return " : ".join(result)
