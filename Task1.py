class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

p1 = BinaryTree(TreeNode(1, TreeNode(2), TreeNode(3)))
q1 = BinaryTree(TreeNode(1, TreeNode(2), TreeNode(3)))
print(is_same_tree(p1.root, q1.root))

p2 = BinaryTree(TreeNode(1, TreeNode(2)))
q2 = BinaryTree(TreeNode(1, None, TreeNode(2)))
print(is_same_tree(p2.root, q2.root))

p3 = BinaryTree(TreeNode(1, TreeNode(2), TreeNode(1)))
q3 = BinaryTree(TreeNode(1, TreeNode(1), TreeNode(2)))
print(is_same_tree(p3.root, q3.root)) 
