def consecutiveNumbersSum(N):
    count = 1
    for k in range(2, int((2*N)**0.5) + 1):
        if ((N - (k * (k - 1) / 2)) % k == 0):
            count = count + 1
    return count
