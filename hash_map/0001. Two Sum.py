"""

Runtime: 100 ms, faster than 32.18% of Python3 online submissions for Two Sum.
Memory Usage: 15.3 MB, less than 31.49% of Python3 online submissions for Two Sum.

https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time

http://www.pythontutor.com/visualize.html#code=def%20twoSum%28numbers,%20target%29%3A%0A%20%20%20%20%20%20%20%20d%20%3D%20%7B%7D%0A%20%20%20%20%20%20%20%20for%20i,%20n%20in%20enumerate%28numbers%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20target%20-%20n%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20m%20in%20d%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20%5Bd%5Bm%5D,%20i%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20d%5Bn%5D%20%3D%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0AtwoSum%28%5B5,%2011,%201,%203,%2010,%202,7%5D,%209%29&cumulative=false&curInstr=32&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

def twoSum(self, numbers, target):
    d = {}
    for i, n in enumerate(numbers): 
        m = target - n
        if m in d: #if key in dict
            return [d[m], i] #return the index, not values
        else:
            d[n] = i
