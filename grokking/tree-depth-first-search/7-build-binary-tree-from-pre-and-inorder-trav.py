
from utils import TreeNode

# input: preorder array and inorder array
# output: binary tree built based on both arrays

# init p_index to 0 to rep index of preorder array (root of tree)
# init hash_map to hold value: idx as key:value pairs
# populate hash_map with for loop range(len(i_order))

# create helper for recursive traversal
# pass in both arrays, left index, right index, hash_map, and p_index
# base case if left > right no more nodes left to construct
# init current to p_index[0] of p_order
# increment p_index[0] += 1
# create root node using current
# if left == right return root
# find the index of current in in_order array in_index = mapping[curr]
# root.left = helper(p_order, i_order, left, in_index - 1, hash_map, p_index)
# root.right = helper(p_order, i_order, in_index + 1, right, hash_map, p_index)
# return root

# time O(n) for each element in preorder/inorder array
# space O(n) for map

def recursive_helper(p_order, i_order, left, right, hash_map, p_index):
    if left > right:
        return None

    current = p_order[p_index[0]]
    p_index[0] += 1

    root = TreeNode(current)

    if left == right:
        return root

    in_index = hash_map[current]

    root.left = recursive_helper(p_order, i_order, left, in_index - 1, hash_map, p_index)
    root.right = recursive_helper(p_order, i_order, in_index + 1, right, hash_map, p_index)

    return root


def build_tree(p_order, i_order):
    p_index = [0]
    hash_map = {}

    for idx in range(len(i_order)):
        hash_map[i_order[idx]] = idx

    root = recursive_helper(p_order, i_order, 0, len(p_order) - 1, hash_map, p_index)

    return root


print(build_tree([3,9,20,15,7],[9,3,15,20,7]))
