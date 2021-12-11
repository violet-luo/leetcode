def maxSubjectsNumber(answered, needed, q):
    diffs = [a - b for a, b in zip(needed, answered)]
    diffs = [0 if i < 0 else i for i in diffs] # answered > negative
    diffs.sort()
    
    counter = 0
    while diffs and q > 0:
        subject = diffs.pop(0)
        if q > subject:
            q -= subject
            counter += 1
    return counter
