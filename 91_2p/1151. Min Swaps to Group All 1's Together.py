def minSwaps(data):
    ones = sum(data)
    
    slow, fast = 0,0
    maxOnes, curOnes = 0,0
    
    # 找到拥有最多1的sliding window
    while fast < len(data):
        if fast - slow < ones: # fast先走到len(ones)
            if data[fast] == 1:
                curOnes += 1
                maxOnes = max(maxOnes, curOnes)
            fast += 1
        else:
            if data[slow] == 1:
                curOnes -= 1
            slow += 1
    return ones - maxOnes
