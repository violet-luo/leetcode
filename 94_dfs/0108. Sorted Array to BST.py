def sortedArrayToBST(self, nums):    
   return convert(0, len(nums) - 1)
def convert(left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    node = TreeNode(nums[mid])
    node.left = convert(left, mid - 1)
    node.right = convert(mid + 1, right)
    return node