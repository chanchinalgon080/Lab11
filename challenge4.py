class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    count = [0]
    result = [None]

    def inorder(node):
        if node is None or result[0] is not None:
            return

        inorder(node.left)

        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def build_bst(vals):
    root = None
    for v in vals:
        root = insert_into_bst(root, v)
    return root

# Test cases
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # 🎯 Second smallest
# 📊 Minimum value
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)
# � Maximum value
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)
# � Middle element
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)
print(kth_smallest(build_bst([10]), 1) == 10)  