from collections import defaultdict
from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    min_column, max_column = float('inf'), float('-inf')
    min_heap = [(0, root)]

    while min_heap:
        column, node = heappop(min_heap)
        if node:
            column_table[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            heappush(min_heap, (column - 1, node.left))
            heappush(min_heap, (column + 1, node.right))

    result = []
    for col in range(min_column, max_column + 1):
        result.append(column_table[col])

    return result


root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
result1 = vertical_order_traversal(root1)

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
result2 = vertical_order_traversal(root2)

root3 = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(6)), TreeNode(3, TreeNode(4), TreeNode(7)))
result3 = vertical_order_traversal(root3)
