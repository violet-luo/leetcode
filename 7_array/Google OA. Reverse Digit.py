def reverse_digits2(n):
    num_str = str(n)
    arr = []
    for i in range(len(num_str)):
        for j in range(i+2, len(num_str)+1):
            arr.append(num_str[:i]+num_str[i:j][::-1]+num_str[j:])
    return max(n, int(max(arr)))
