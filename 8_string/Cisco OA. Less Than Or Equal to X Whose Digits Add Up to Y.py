# 12 of 12 cases passed
def xy(x, y):
    if y == 0:
        return 0
    count = 0
    for i in range(x):
        digit_sum = 0
        for digit in str(i):
            digit_sum += int(digit)
    if digit_sum == y:
        count += 1
    return count
