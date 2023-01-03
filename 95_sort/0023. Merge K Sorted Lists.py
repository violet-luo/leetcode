def mergekSortedArrays(self, arrays):
    return self.merge_range_arrays(arrays, 0, len(arrays) - 1)
    
# 标准归排
def merge_range_arrays(self, arrays, start, end):
    if start == end:
        return arrays[start]
    
    mid = (start + end) // 2
    left = self.merge_range_arrays(arrays, start, mid)
    right = self.merge_range_arrays(arrays, mid + 1, end)
    return self.merge_two_arrays(left, right)

def merge_two_arrays(self, arr1, arr2):
    i, j = 0, 0
    array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            array.append(arr1[i])
            i += 1
        else:
            array.append(arr2[j])
            j += 1
    while i < len(arr1):
        array.append(arr1[i])
        i += 1
    while j < len(arr2):
        array.append(arr2[j])
        j += 1
    return array
