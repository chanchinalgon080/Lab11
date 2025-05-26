class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_bst(values):
    """Build a BST from a list of values"""
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        insert_bst(root, val)
    return root

def insert_bst(root, val):
    """Insert a value into the BST"""
    if val < root.val:
        if root.left:
            insert_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_bst(root.right, val)
        else:
            root.right = TreeNode(val)

def find_lca(root, val1, val2):
    """Find lowest common ancestor of two values in BST"""
    while root:
        if val1 < root.val and val2 < root.val:
            root = root.left
        elif val1 > root.val and val2 > root.val:
            root = root.right
        else:
            return root.val
    return None

# ✅ Test cases
# Test 1: Values in different subtrees
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 2, 8
# Expected: 6
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # 🌲 Root as LCA

# Test 2: Values in same subtree
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 0, 4
# Expected: 2
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # 📊 Subtree LCA

# Test 3: One value is ancestor of other
# BST: [6, 2, 8, 0, 4, 7, 9, 3, 5]
# Values: 2, 3
# Expected: 2
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # 🔗 Ancestor relationship

# Test 4: Same values
# BST: [5, 3, 7]
# Values: 5, 5
# Expected: 5
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)  # 🎯 Same node

# Test 5: Values at leaf level
# BST: [4, 2, 6, 1, 3, 5, 7]
# Values: 1, 3
# Expected: 2
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)  # 🌱 Leaf nodes
