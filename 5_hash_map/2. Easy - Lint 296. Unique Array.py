def getUniqueArray(self, arr):
    isVisited = {}

    n = len(arr)

    uniqueArray = []

    for i in range(n):
        if not arr[i] in isVisited:
            isVisited[arr[i]] = True
            uniqueArray.append(arr[i])

    return uniqueArray
