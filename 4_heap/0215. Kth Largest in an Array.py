# 1. Heap
import heapq
class Solution(object):
	def findKthLargest(nums, k):
	    minHeap = []
	    for num in nums:
	        heapq.heappush(minHeap, num) # push the heap value onto the heap #[1,3,2]
	        if len(minHeap) > k:
	            heapq.heappop(minHeap) # pop and return the smallest item from the heap #[3,2]
	    return minHeap[0] #[5,6]

def findKthLargest(self, nums: List[int], k: int) -> int:
    minHeap = []
    for x in nums:
        heappush(minHeap, x)
        if len(minHeap) > k:
            heappop(minHeap)
    return minHeap[0]

# 2. Quick Select
def findKthLargest(self, nums: List[int], k: int) -> int:
    pos = self.partition(nums, 0, len(nums)-1)
    if pos > len(nums) - k:
        return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
    elif pos < len(nums) - k:
        return self.findKthLargest(nums[pos+1:], k)
    else:
        return nums[pos]

def partition(self, nums, l, r):
    pivot = nums[r]
    lo = l 
    for i in range(l, r):
        if nums[i] < pivot:
            nums[i], nums[lo] = nums[lo], nums[i]
            lo += 1
    nums[lo], nums[r] = nums[r], nums[lo]
    return lo
