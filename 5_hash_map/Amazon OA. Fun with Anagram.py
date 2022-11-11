def funWithAnagrams(arr):
    res = []
    seen = set()
 
    for word in arr:
        anagram = "".join(sorted(word))
        if anagram not in seen:
            seen.add(anagram)
            res.append(word)
    return sorted(res)
