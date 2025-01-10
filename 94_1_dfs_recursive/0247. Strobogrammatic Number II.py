def findStrobogrammatic(self, n: int) -> List[str]:
    dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    def traverse(x: int) -> List[str]:
        # base case
        if x == 0:
            return ['']
        if x == 1:
            return ['0', '1', '8']

        smaller_numbers = traverse(x - 2)
        res = []

        for num in smaller_numbers:
            for key, val in dic.items():
                if x == n and key == '0':
                    continue
                res.append(key + num + val)
        
        return res
