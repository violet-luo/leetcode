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
