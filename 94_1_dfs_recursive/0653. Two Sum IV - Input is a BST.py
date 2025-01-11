def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    found_target = False
    seen = set() # 用set()是O(1), 用[]是O(n)

    def traverse(node):
        nonlocal found_target, seen
        if node is None:
            return None
        
        traverse(node.left)
        if (k - node.val) in seen:
            found_target = True
        seen.add(node.val)

        traverse(node.right)
    
    traverse(root)
    return found_target
