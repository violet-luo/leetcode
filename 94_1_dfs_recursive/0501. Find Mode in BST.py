def findMode(self, root: Optional[TreeNode]) -> List[int]:
    current_val = None
    current_count = 0
    max_count = 0
    modes = []

    def traverse(node):
        nonlocal current_val, current_count, max_count, modes
        if not node:
            return
        
        traverse(node.left)

        if node.val == current_val:
            current_count += 1
        else:
            current_count = 1
            current_val = node.val
        
        if current_count == max_count:
            modes.append(node.val)
        elif current_count > max_count:
            max_count = current_count
            modes = [node.val]
        
        traverse(node.right)
    
    traverse(root)
    return modes
    
###

def findMode(self, root):
    nums = self.inorder(root)
    counter = collections.Counter(nums)
    for num in nums:
        counter[num] += 1
    mode = max(counter.values())
    return [key for key in counter.keys() if counter[key] == mode]

def inorder(self, root):
    if not root:
        return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)
