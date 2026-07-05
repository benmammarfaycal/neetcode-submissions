class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]in nums[i+1:] or i>0 and nums[i] in nums[0:i]:
                continue
            else:
                return nums[i]