"""

Runtime: 76 ms, faster than 73.95% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.2 MB, less than 25.03% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35224/Python-optimal-solution

"""

def sortedArrayToBST(self, nums: List[int]) -> TreeNode:    
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)
