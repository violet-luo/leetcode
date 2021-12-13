def two_sum_unique_pairs(n, itemValues, target):
    visited = set()
    complement = set()
    for item in itemValues:
        if not item in complement:
            complement.add(target - item)
        else:
            visited.add((item, target - item))
            print(item, target - item)
    return len(visited)
