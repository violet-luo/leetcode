def numJewelsInStones(jewels, stones):
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
        
    return count
  
  ### 
  
def numJewelsInStones(self, jewels, stones):
    return sum(s in jewels for s in stones)
