from collections import defaultdict
def get_common_ancestor(parent_child_pairs, n1, n2):
    # 1. 先建图
    parent_child_map = defaultdict(list)
    for parent, child in parent_child_pairs:
        parent_child_map[child].append(parent)

    def get_ancestors(node):
        stack = [node] # 只有一个int, 用collections.deque is not iterable
        ancestors = set()
        while stack:
            curr = stack.pop()
            for parent in parent_child_map[curr]:
                ancestors.add(parent)
                stack.append(parent)
        return ancestors

    n1_parents = get_ancestors(n1)
    n2_parents = get_ancestors(n2)
    for n in n1_parents:
        if n in n2_parents:
            return True
    return False
