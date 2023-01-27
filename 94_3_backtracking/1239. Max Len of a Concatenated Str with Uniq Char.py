def maxLength(self, arr):
    result = 0
    temp = []

    # 检查是否满足字符唯一的条件
    def can_add(current, temp):
        concat_str = ''.join(temp)
        for c in current:
            if c in concat_str:
                return False
        return True

    # 检查字符串本身有没有重复的字符
    def is_distinct(current):
        return len(set(current)) == len(current)

    def backtrack(start, temp, arr): 
        nonlocal result 
        result = max(result, len(''.join(temp)))

        for i in range(start, len(arr)):
            if can_add(arr[i], temp) and is_distinct(arr[i]):
                temp.append(arr[i])
                backtrack(i+1, temp, arr)
                temp.pop(-1)

    backtrack(0, temp, arr)
    return result
