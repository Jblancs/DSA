# input: root
# output: lowest common ancestor

# init tracking variables mid, left and right

# helper for recursive trav
# pass in current_node, p, q, mid, left, right

# time: O(n) where n is number of nodes
# space: O(h)

class Solution:
    def __init__(self):
        self.lca = None

    def lowest_common_ancestor(self, root, p, q):
        self.lowest_common_ancestor_rec(root, p, q)
        # Replace this placeholder return statement with your code
        return self.lca

    def lowest_common_ancestor_rec(self, current_node, p, q):

