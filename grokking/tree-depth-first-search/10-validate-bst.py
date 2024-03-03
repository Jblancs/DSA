import math

def validate_bst_rec(root, prev):
    if not root:
        return True

    if not validate_bst_rec(root.left, prev):
        return False

    if root.data <= prev[0]:
        return False

    prev[0] = root.data

    return validate_bst_rec(root.right, prev)

def validate_bst(root):
    prev = [float("-inf")]
    result = validate_bst_rec(root, prev)
    return result
