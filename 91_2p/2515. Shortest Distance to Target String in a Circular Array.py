def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
    n = len(words)
    long_words = words + words + words

    target_idx = []
    for i, word in enumerate(long_words):
        if word == target:
            target_idx.append(i)
    
    startIndex = n + startIndex
    min_dist = float('inf')

    for i in range(n):
        if long_words[startIndex + i] == target or long_words[startIndex - i] == target:
            return i
    
    return -1
