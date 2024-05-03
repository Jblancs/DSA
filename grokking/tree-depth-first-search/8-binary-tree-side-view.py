# input root
# output: right side view (data of nodes visible when tree is viewed from right)
# init rside to empty array for storing right most nodes

# time: O(n) for each node
# time: O(h) for array with len of height of tree

def dfs(rside, node, level):
    length = len(rside)

    if length == level:
        rside.append(node.data)

    if node.right:
        dfs(rside, node.right, level + 1)
    if node.left:
        dfs(rside, node.left, level + 1)




def right_side_view(root):
    res = []
    dfs(res, root, 0)
    return res
