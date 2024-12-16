def findStrobogrammatic(self, n: int) -> List[str]:
    pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

    def traverse(x: int) -> List[str]:
        # base case
        if x == 0:
            return ['']
        if x == 1:
            return ['0', '1', '8']

        smaller_numbers = traverse(x - 2)
        res = []

        for num in smaller_numbers:
            for pair in pairs:
                # Avoid leading zeros when x == n
                if x == n and pair[0] == '0':
                    continue
                res.append(pair[0] + num + pair[1])
        
        return res
    
    return traverse(n)
