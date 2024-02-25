# input root
# output: max sum of any non empty path

# init a sum to hold the total of a given path

# create helper
# total = root.value
# base case: if root.left and root.right = None return root.value
# init left_sum to recursive call and pass in left node
# if root.left total += root.left
# if root.right total += root.right
# if total > sum: sum = total
# init right_sum to recursive call and pass in right node
# if root.left total += root.left
# if root.right total += root.right
# if total > sum: sum = total

def max_contrib(root, sum):
    if not root:
        return 0

    max_left = max_contrib(root.left)
    max_right = max_contrib(root.right)

    left_tree = 0
    right_tree = 0

    if left_tree > 0:
        left_tree = max_left
    if right_tree > 0:
        right_tree = max_right

    value_new_path = root.data + left_tree + right_tree

    max_sum = max_contrib.max_sum
    max_contrib.max_sum = max(max_sum, value_new_path)

    return root.data + max(left_tree, right_tree)



def max_path_sum(root):
    max_contrib.max_sum = float("-inf")

    max_contrib(root)

    return max_contrib.max_sum
