def isPrime(n, nums):
    res = ''
    for num in nums:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                res += ' ' + 'Composite'
                break
        else:
            res += ' ' + 'Prime'
    return res
