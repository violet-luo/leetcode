"""

1. Sort

Runtime: 92 ms, faster than 91.04% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.1 MB, less than 94.04% of Python3 online submissions for Group Anagrams.

"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = {}

    for str in strs:
        key_str = ''.join(sorted(str))
        if key_str in dic:
            dic[key_str].append(str)
        else:
            dic[key_str] = [str]
    return list(dic.values())
  
  
"""

2. Hash Map

Runtime: 284 ms, faster than 5.09% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.3 MB, less than 20.07% of Python3 online submissions for Group Anagrams.

Visualization: http://www.pythontutor.com/visualize.html#code=import%20collections%0A%0Adef%20groupAnagrams%28strs%29%3A%0A%20%20%20%20mp%20%3D%20collections.defaultdict%28list%29%0A%20%20%20%20%0A%20%20%20%20for%20st%20in%20strs%3A%0A%20%20%20%20%20%20%20%20counts%20%3D%20%5B0%5D%20*%2026%0A%20%20%20%20%20%20%20%20for%20ch%20in%20st%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20counts%5Bord%28ch%29%20-%20ord%28%22a%22%29%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20mp%5Btuple%28counts%29%5D.append%28st%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20list%28mp.values%28%29%29%0A%20%20%20%20%0AgroupAnagrams%28%5B%22eat%22,%22tea%22,%22tan%22,%22ate%22,%22nat%22,%22bat%22%5D%29&cumulative=false&curInstr=24&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # if a key is not found in the dict, create a new key
    mp = collections.defaultdict(list)

    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord("a")] += 1 #convert a char into its Unicode
            print(counts)
        mp[tuple(counts)].append(st)

    return list(mp.values())
