from utils import TreeNode


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
