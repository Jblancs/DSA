# init diameter to 0
# create helper function that takes in root and diam
# unpack function to _, diameter
# in helper function
# 

def diameter_helper(node, diameter):
    if node is None:
        return 0, diameter

    else:
        lh, diameter = diameter_helper(node.left, diameter)
        rh, diameter = diameter_helper(node.right, diameter)

        diameter = max(diameter, lh + rh)

        return max(lh, rh) + 1, diameter

def diameter_of_binaryTree(root):
    diameter = 0

    _, diameter = diameter_helper(root, diameter)

    return
