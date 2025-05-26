class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    """Check if binary tree is a valid BST using recursive min/max bounds."""

    def helper(node, low, high):
        # An empty node is valid
        if not node:
            return True

        # Current node value must be strictly between low and high bounds
        if not (low < node.val < high):
            return False

        # Recursively validate left subtree with updated upper bound
        if not helper(node.left, low, node.val):
            return False

        # Recursively validate right subtree with updated lower bound
        if not helper(node.right, node.val, high):
            return False

        return True

    # Initialize with infinite bounds
    return helper(root, float('-inf'), float('inf'))

# Helper to build tree from list (level order)


def build_tree(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kid_index = 1
    for i in range(len(vals)):
        if nodes[i] is not None:
            if kid_index < len(vals):
                nodes[i].left = nodes[kid_index]
                kid_index += 1
            if kid_index < len(vals):
                nodes[i].right = nodes[kid_index]
                kid_index += 1
    return nodes[0]


def build_invalid_tree1():
    # Tree:    5
    #         / \
    #        6   7  (left child > root violates BST)
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    return root


def build_invalid_tree2():
    # Tree:    5
    #         / \
    #        3   4  (right child < root violates BST)
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root


# Test cases
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)  # Valid BST
print(is_valid_bst(build_invalid_tree1())
      == False)             # Left violation
print(is_valid_bst(build_invalid_tree2()) ==
      False)             # Right violation
# Single node valid
print(is_valid_bst(build_tree([42])) == True)
# Empty tree valid
print(is_valid_bst(None) == True)
