class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# функция обхода
def Obhod(root):
    if not root:
        return []

    result = []
    current_level = [root]

    while current_level:
        level_values = []    
        next_level = []

        for node in current_level:
            level_values.append(node.val)
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        result.append(level_values)
        
        current_level = next_level
        
    return result


root = TreeNode(9)
root.left = TreeNode(16)
root.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.right = TreeNode(11)

print(Obhod(root)) 