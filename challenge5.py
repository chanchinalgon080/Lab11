class Node:
    def __init__(self, val):
        self.val = val
        self.left = None  
        self.right = None 
def bst_to_dll(root):
    def inorder(node):
        nonlocal first, last
        if not node:
            return

        inorder(node.left)

        if last:
            last.right = node
            node.left = last
        else:
            first = node  

        last = node
        inorder(node.right)

    if not root:
        return None

    first, last = None, None
    inorder(root)

    last.right = first
    first.left = last

    return first

def build_bst(values):
    """Builds a balanced BST from a sorted list"""

    def insert_level_order(arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(arr[mid])
        node.left = insert_level_order(arr, start, mid - 1)
        node.right = insert_level_order(arr, mid + 1, end)
        return node

    return insert_level_order(sorted(values), 0, len(values) - 1)

def build_degenerate_bst(values):
    if not values:
        return None
    root = Node(values[0])
    current = root
    for val in values[1:]:
        current.right = Node(val)
        current = current.right
    return root

def validate_circular_dll(head, expected_vals):
    if not head and not expected_vals:
        return True
    if not head or not expected_vals:
        return False

    current = head
    forward = []
    for _ in range(len(expected_vals)):
        forward.append(current.val)
        current = current.right
        if current == head:
            break
    if forward != expected_vals:
        return False

    current = head.left
    backward = []
    for _ in range(len(expected_vals)):
        backward.append(current.val)
        current = current.left
        if current == head.left:
            break
    if backward != expected_vals[::-1]:
        return False

    return True

# Test 1: Simple BST
head1 = bst_to_dll(build_bst([2, 1, 3]))
print("Test 1 Passed:", validate_circular_dll(head1, [1, 2, 3]))

# Test 2: Larger BST
head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print("Test 2 Passed:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]))

# Test 3: Single node
head3 = bst_to_dll(build_bst([5]))
print("Test 3 Passed:", validate_circular_dll(head3, [5]))

# Test 4: Degenerate BST (like linked list)
head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print("Test 4 Passed:", validate_circular_dll(head4, [1, 2, 3, 4]))

# Test 5: Empty tree
head5 = bst_to_dll(None)
print("Test 5 Passed:", head5 is None)


