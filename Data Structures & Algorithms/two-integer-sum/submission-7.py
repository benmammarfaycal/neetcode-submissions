class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         count = {}
         for i, num in enumerate(nums):
             complement = target - num
             if complement in count:
                 return [count[complement], i] 
             count[num] = i