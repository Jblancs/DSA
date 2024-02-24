from utils import TreeNode

MARKER = "M"
m = 1

def serialize_rec(node, stream):
    global m

    if node is None:
        stream.append(MARKER + str(m))
        m += 1
        return

    stream.append(node.data)

    serialize_rec(node.left, stream)
    serialize_rec(node.right, stream)

def serialize(root):
    stream = []
    serialize_rec(root, stream)
    return stream

def deserialize_helper(stream):
    val = stream.pop()

    if type(val) is str and val[0] == MARKER:
        return None

    node = TreeNode(val)

    node.left = deserialize_helper(stream)
    node.right = deserialize_helper(stream)

    return node

def deserialize(stream):
    stream.reverse()
    node = deserialize_helper(stream)
    return node
