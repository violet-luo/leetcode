def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    prev_parent = None
    prev_right = None
    head = root

    while head:
      # 因为后面要断开这个连接，所以存储left是之后的head, right是之后的左叶子
      left = head.left
      right = head.right
      # 往上翻转
      head.right = prev_parent
      head.left = prev_right
      # move next
      prev_parent = head
      prev_right = right
      head = left

    return prev_parent
