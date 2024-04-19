

def mirror_binary_tree(root):
    if root is None:
        return None

    if root.left:
        left = mirror_binary_tree(root.left)

    if root.right:
        right = mirror_binary_tree(root.right)

    root.left = right
    root.right = left

    return root
