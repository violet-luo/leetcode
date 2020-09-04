"""

# 1. recursion

Runtime: 28 ms, faster than 84.98% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.6 MB, less than 95.23% of Python3 online submissions for Invert Binary Tree.

https://leetcode.com/problems/invert-binary-tree/discuss/62705/Python-solutions-(recursively-dfs-bfs).

"""

def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root


# 2. DFS iterative
def invertTree(self, root):
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop(0)
        if node: 
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root


# 3. BFS
def invertTree(self, root):
    if not root:
        return None

    queue = collections.deque([(root)])
    while queue:
        node = queue.pop（0）
        if node.left or node.right:
            node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
