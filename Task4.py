class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right


root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
k1 = 1
result1 = kth_smallest(root1, k1)

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
k2 = 3
result2 = kth_smallest(root2, k2)

