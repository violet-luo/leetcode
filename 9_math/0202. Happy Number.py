def isHappy(self, n: int) -> bool:
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n //= 10
        n = sum
    return n == 1
