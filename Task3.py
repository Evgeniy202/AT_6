class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
result1 = invert_tree(root1)

root2 = TreeNode(2, TreeNode(1), TreeNode(3))
result2 = invert_tree(root2)

root3 = None
result3 = invert_tree(root3)

