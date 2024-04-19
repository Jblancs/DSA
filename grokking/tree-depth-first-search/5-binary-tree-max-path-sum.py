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
    if root is None:
        return 0





def max_path_sum(root):
    sum = float("-inf")

    max_contrib(root, sum)

    return sum
