class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder):
    def helper(lower=float('-inf'), upper=float('inf')):
        nonlocal idx
        if idx == len(preorder):
            return None

        val = preorder[idx]
        if val < lower or val > upper:
            return None

        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)

        return root

    idx = 0
    return helper()


traversal1 = "1-2--3--4-5--6--7"
result1 = build_tree(list(map(int, traversal1.split('-'))))

traversal2 = "1-2--3---4-5--6---7"
result2 = build_tree(list(map(int, traversal2.split('-'))))

traversal3 = "1-401--349---90--88"
result3 = build_tree(list(map(int, traversal3.split('-'))))
