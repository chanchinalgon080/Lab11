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

def range_query(root, min_val, max_val):
    """Find all values in BST within given range [min_val, max_val]"""
    result = []

    def inorder(node):
        if not node:
            return
        if node.val > min_val:
            inorder(node.left)
        if min_val <= node.val <= max_val:
            result.append(node.val)
        if node.val < max_val:
            inorder(node.right)

    inorder(root)
    return result

# ✅ Test cases
# Test 1: Normal range
# BST: [1, 3, 5, 7, 9, 11, 13]
# Range: [5, 10]
# Expected: [5, 7, 9]
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])  # 🎯 Normal range

# Test 2: Full range
# BST: [2, 4, 6, 8]
# Range: [1, 10]
# Expected: [2, 4, 6, 8]
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])  # 📊 Full coverage

# Test 3: No values in range
# BST: [10, 20, 30]
# Range: [1, 5]
# Expected: []
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])  # 📭 Empty result

# Test 4: Single value
# BST: [15]
# Range: [10, 20]
# Expected: [15]
print(range_query(build_bst([15]), 10, 20) == [15])  # 🌱 Single node

# Test 5: Edge values
# BST: [5, 10, 15, 20, 25]
# Range: [10, 20]
# Expected: [10, 15, 20]
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])  # 🔗 Include boundaries
