def intToRoman(self, n):
    rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    digit = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    
    for d, r in zip(digit, rom):
        result += r * (n // d)
        n %= d 
    return result
