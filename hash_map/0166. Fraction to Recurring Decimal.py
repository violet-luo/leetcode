"""

Runtime: 24 ms, faster than 95.46% of Python3 online submissions for Fraction to Recurring Decimal.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.

"""

def fractionToDecimal(self, numerator, denominator):
    num, den = numerator, denominator
    if not den:  # denominator is 0
        return 
    if not num:  # numerator is 0
        return "0"
    res = []
    if (num < 0) ^ (den < 0):
        res.append("-")  # add the sign
    num, den = abs(num), abs(den)
    res.append(str(num//den))
    rmd = num % den
    if not rmd:
        return "".join(res)  # only has integral part
    res.append(".")  # has frational part
    dic = {}
    while rmd:
        if rmd in dic:   # the remainder recurs
            res.insert(dic[rmd], "(")
            res.append(")")
            break
        dic[rmd] = len(res) 
        div, rmd = divmod(rmd*10, den)
        res.append(str(div))
    return "".join(res)
