class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        
        return ",".join(result) # 1,2,3,None,None,4,5,None,None,None,None

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        
        nodes = data.split(",") # ['1', '2', '3', 'None', 'None', '4', '5', 'None', 'None', 'None', 'None']
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1 # 从root后的点开始
        
        while queue:
            node = queue.popleft()
            if nodes[index] != "None":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != "None":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
