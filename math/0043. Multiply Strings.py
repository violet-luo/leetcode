def multiply(self, num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    n = len(num1) + len(num2)
    res = [0] * n
    # 模拟乘法竖式计算
    for i in range(len(num1) - 1,-1,-1):
        for j in range(len(num2) - 1,-1,-1):
            res[i + j + 1] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
    # 处理进位
    for i in range(n - 1,0,-1):
        res[i - 1] += res[i] // 10;
        res[i] %= 10;
    ans = ""
    # 将数组转换为字符串
    for i in range(n):
        if  res[i] == 0 and ans == "": #处理前导零
            continue
        ans += chr(res[i] + ord('0'));
    return ans;
