"""
Credit to @leetcodeftw

Explanation: All the numbers are positive. Once we visit a number, we make it negative and return the indexes of the positive 
numbers we have not visitied.

Demo: http://www.pythontutor.com/visualize.html#code=def%20findDisappearedNumbers%28nums%29%3A%0A%20%20%20%20for%20num%20in%20nums%3A%0A%20%20%20%20%20%20%20%20index%20%3D%20abs%28num%29%20-%201%0A%20%20%20%20%20%20%20%20nums%5Bindex%5D%20%3D%20-abs%28nums%5Bindex%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20%5Bi%20%2B%201%20for%20i,%20num%20in%20enumerate%28nums%29%20if%20num%20%3E%200%5D%0A%20%20%20%20%0A%20%20%20%20%0Anums%20%3D%20%5B4,3,2,7,8,2,3,1%5D%0Amissing%20%3D%20%5B%5D%0A%0AfindDisappearedNumbers%28nums%29&cumulative=false&curInstr=41&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])
            
    return [i + 1 for i, num in enumerate(nums) if num > 0]
