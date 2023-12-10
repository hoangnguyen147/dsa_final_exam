class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    new_node = TreeNode(data)
    if root is None:
        return TreeNode(data)
    
    current_node = root

    while current_node is not None:
        if data == current_node.data:
            return root
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
                return root
            else:
                current_node = current_node.left
        else:
            if current_node.right is None:
                current_node.right = new_node
                return root
            else:
                current_node = current_node.right
            
def findAncestors(root, k):
    results = []
    current_node = root
    while current_node is not None:
        if current_node.data == k:
            results.reverse()
            return results
        
        if current_node.data > k:
            results.append(current_node.data)
            current_node = current_node.left
        else:
            results.append(current_node.data)
            current_node = current_node.right

    return results

def preorder_traversal(root):
    result = []
    stack = [root]
    while stack:
        current_node = stack.pop()
        if current_node:
            result.append(current_node.data)
            stack.append(current_node.right)
            stack.append(current_node.left)
    print(result)
    return result

    
root = TreeNode(6)
insert(root, 4)
insert(root, 2)
insert(root, 5)
insert(root, 9)
insert(root, 8)
insert(root, 12)
insert(root, 10)
insert(root, 14)
preorder_traversal(root)
print(findAncestors(root, 10))
