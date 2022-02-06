def reverse_digits(n):
    num_str = str(n)
    max_num = n
    for i in range(len(num_str) - 1):
        for j in range(i+1, len(num_str)):
            if int(num_str[i]) < int(num_str[j]):
                reverse_str = num_str[:i]+num_str[i:j+1][::-1]+num_str[j+1:]
                max_num = max(max_num, int(reverse_str))
    return max_num
