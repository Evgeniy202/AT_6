class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        node_path_sum = node.val + left_gain + right_gain

        max_sum = max(max_sum, node_path_sum)

        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
result1 = max_path_sum(root1)

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result2 = max_path_sum(root2)
