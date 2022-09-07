def compareVersion(self, version1: str, version2: str) -> int:
    list1 = [int(v) for v in version1.split(".")]
    list2 = [int(v) for v in version2.split(".")]

    list1_len = len(list1)
    list2_len = len(list2)

    # 1 vs 1.1
    for i in range(max(list1_len, list2_len)): 
        v1 = list1[i] if i < list1_len else 0
        v2 = list2[i] if i < list2_len else 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    return 0
