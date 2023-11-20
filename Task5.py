class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return "[]"

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    return "[" + ",".join(result) + "]"

def deserialize(data):
    if data == "[]":
        return None

    values = data[1:-1].split(",")
    root = TreeNode(int(values[0]))
    queue = [root]
    index = 1

    while queue:
        node = queue.pop(0)

        left_val = values[index]
        index += 1
        if left_val != "null":
            node.left = TreeNode(int(left_val))
            queue.append(node.left)

        right_val = values[index]
        index += 1
        if right_val != "null":
            node.right = TreeNode(int(right_val))
            queue.append(node.right)

    return root


root1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized1 = serialize(root1)
print(serialized1)
deserialized1 = deserialize(serialized1)

root2 = None
serialized2 = serialize(root2)
print(serialized2)
deserialized2 = deserialize(serialized2)

