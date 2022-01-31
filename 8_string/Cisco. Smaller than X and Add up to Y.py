def xy(x, y):
    count = 0
    for i in range(x):
        digit_sum = 0
        for digit in str(i):
            digit_sum += int(digit)
        if digit_sum == y:
            count += 1
    return count

xy(20, 5)
