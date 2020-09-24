"""

Runtime: 136 ms, faster than 96.35% of Python3 online submissions for Count Primes.
Memory Usage: 37 MB, less than 25.62% of Python3 online submissions for Count Primes.

"""

def countPrimes(self, n: int) -> int:
    # Sieve of Eratosthenes

    if n < 2:
        return 0

    lst = [1] * n    # create a list for marking numbers less than n   
    lst[0] = lst[1] = 0    # 0 and 1 are not prime numbers

    m = 2
    while m * m < n:    # only check a number (m) if its square is less than n
        if lst[m] == 1:
            # mark all its multiples from m * m to n by 0
            # m*m:n:m: 从m*m到n 的index 每个间隔m个
            # 1 + (n - m * m - 1)：从 m*m 到n 每个间隔m个index，补充进去的list要和抽出来的batch一样长
            lst[m * m: n: m] = [0] * (1 + (n - m*m - 1) // m)

        # If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1;     
        m += 1 if m == 2 else 2
    return sum(lst)
