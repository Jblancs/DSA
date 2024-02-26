# input root
# output: right side view (data of nodes visible when tree is viewed from right)
# init rside to empty array for storing right most nodes

# time: O(n) for each node
# time: O(h) for array with len of height of tree

def dfs(rside, node, level):
    if len(rside) == level:
        rside.append(node)

    for child in [node.right, node.left]:
        if child:
            dfs(rside, child, level + 1)

def right_side_view(root):
    if root is None:
        return []

    rside = []

    dfs(rside, root, level = 0)

    return rside
