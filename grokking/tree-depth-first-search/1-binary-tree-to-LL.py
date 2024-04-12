from utils import TreeNode

# edge case if root is None return
# init current to root
# while loop to iterate while current is exists
# if current.left exists find the right most node of the left subtree
# init last to current.left
# while last.right to iterate until right most node
# last = last.right
# assign last.right to current.right
# assign current.right to current.left
# assign current.left to None
# outside if statement we reassign current to current.right
# return root


def flatten_tree(root):
    if not root:
        return

    current = root

    while current:

        if current.left:
            last = current.left

            while last.right:
                last = last.right

            last.right = current.right
            current.right = current.left
            current.left = None

        current = current.right

    return root
