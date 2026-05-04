class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapMax=[-x for x in nums]
        heapq.heapify(heapMax)
        while k>0:
            res=heapq.heappop(heapMax)
            k-=1
        return -res