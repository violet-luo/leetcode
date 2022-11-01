def lowestCommonAncestorII(self, root, p, q):
    parent_set = set()

    # 把A的祖先节点加入到哈希表中
    curr = p
    while curr:
        parent_set.add(curr)
        curr = curr.parent

    # 遍历B的祖先节点，第一个在哈希表中出现的即为答案
    curr = q
    while curr:
        if curr in parent_set:
            return curr
        curr = curr.parent
    return None
